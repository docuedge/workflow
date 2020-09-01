#Code for Cognito User SignIn
#Created by : Vikram
#Modified date : 2/23/20

from django.conf import settings
import os
import boto3
import hmac
import hashlib
import base64
import json
import sys, traceback
from rest_framework import exceptions

USER_POOL_ID = settings.COGNITO_USER_POOL_ID
CLIENT_ID = settings.COGNITO_CLIENT_ID
CLIENT_SECRET = settings.COGNITO_CLIENT_SECRET

client = None

def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2

ERROR = 0
SUCCESS = 1
USER_EXISTS = 2

def initiate_auth(username, password):
    resp = None
    try:
        resp = client.admin_initiate_auth(
            UserPoolId=USER_POOL_ID,
            ClientId=CLIENT_ID,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': username,
                'SECRET_HASH': get_secret_hash(username),
                'PASSWORD': password
            },
            ClientMetadata={
                'username': username,
                'password': password
            })
    except client.exceptions.NotAuthorizedException as e:
        traceback.print_exc(file=sys.stdout)
        #raise Exception("400: The username or password is incorrect") #REMOVED
        raise exceptions.ValidationError("400: Username or password is incorrect")
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        exceptions.server_error(e)
    return resp, None



def handler(event):
    global client
    if client == None:
        client = boto3.client('cognito-idp',
                        region_name =  settings.AWS_REGION,
                        aws_access_key_id = settings.ACCESS_KEY,
                        aws_secret_access_key = settings.ACCESS_SECRET
        )
        
    username = event['username']
    password = event['password']
    
    resp, msg = initiate_auth(username, password)
    if msg != None:
        #raise Exception("400: " + msg) #REMOVED
        raise exceptions.ValidationError("400: " + msg)
    
    
        
    access_token = resp['AuthenticationResult']['AccessToken']    
    userInformation = client.get_user(AccessToken=access_token)
    refresh_token = resp['AuthenticationResult']['RefreshToken']
    expiryTime= resp['AuthenticationResult']['ExpiresIn']

    user= {}
    user['id'] = ''
    user['username'] = userInformation['Username']
    user['password'] = ''
    user['firstName'] = ''
    user['lastName'] = ''
    user['token'] = access_token
    user['expiryTime'] = expiryTime
    user['refresh_token'] = refresh_token
    
    
    return user
    