import os
import boto3
import hmac
import hashlib
import base64
import json
from django.conf import settings
from workflow_vault.exceptions import WorkflowException

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


def initiate_refreshtokenauth(username, refreshToken):
    try:
        resp = client.admin_initiate_auth(
            UserPoolId=USER_POOL_ID,
            ClientId=CLIENT_ID,
            AuthFlow='REFRESH_TOKEN_AUTH',
            AuthParameters={
                'REFRESH_TOKEN': refreshToken,
                'SECRET_HASH': get_secret_hash(username)
                
            })
    except client.exceptions.NotAuthorizedException as e:
        raise WorkflowException(400,"ValidationError","The username or refreshToken is incorrect")
    except Exception as e:
        raise WorkflowException(500,"Unknown Error",str(e))
    return resp, None

def initiate_auth(username, password):
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
        raise WorkflowException(400,"ValidationError","The username or password is incorrect")
    except Exception as e:
        raise WorkflowException(500,"Unknown Error",str(e))
    return resp, None



def handler(event):
    global client
    if client == None:
        client = boto3.client('cognito-idp',
                        region_name =  settings.AWS_REGION,
                        aws_access_key_id = settings.ACCESS_KEY,
                        aws_secret_access_key = settings.ACCESS_SECRET
        )
    
    authtype = event['AuthType'] 
    username = None
    password = None
    refreshToken = None
    resp = None
    msg =  None
    refresh_token = None
    
    if(authtype =="Credential"):
        username = event['Credential']['username']
        password = event['Credential']['password']
        resp,msg = initiate_auth(username,password)
        
    if(authtype =="RefreshToken"):
       username=event['RefreshToken']['username']
       refreshToken = event['RefreshToken']['refreshToken']
       resp, msg = initiate_refreshtokenauth(username, refreshToken)
    
   
    
    if msg != None:
     raise WorkflowException(400,"UnknownError",msg)
    
    
        
    access_token = resp['AuthenticationResult']['AccessToken']    
    userInformation = client.get_user(AccessToken=access_token)
    if(authtype =="Credential"):
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
    