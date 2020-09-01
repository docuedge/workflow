from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import status
import boto3
from django.conf import settings
import sys, traceback


class CognitoAuthentication(authentication.TokenAuthentication):

    def authenticate(self, request):
        user = User()
        try:
            client = boto3.client('cognito-idp',
                            region_name =  settings.AWS_REGION,
                            aws_access_key_id = settings.ACCESS_KEY,
                            aws_secret_access_key = settings.ACCESS_SECRET        
            )  
        except (Exception):
            traceback.print_exc(file=sys.stdout)
            msg = ("Connection to Cognito IDP failed")    
            exceptions.server_error(msg)
       
        try:
            authToken = request.META.get('HTTP_AUTHORIZATION', b'')
            token = authToken.split()[1]
            # print(token)
            userInformation = client.get_user(AccessToken=token)
            user.username = userInformation['Username']
            for userAttributes in userInformation['UserAttributes']:
                if userAttributes['Name'] == 'email':
                    user.email = userAttributes['Value']

            groupInformation = client.admin_list_groups_for_user(Username=userInformation["Username"],UserPoolId=settings.COGNITO_USER_POOL_ID)
            groupList = groupInformation['Groups']        
            settings.USER_GROUPS = []
            for group in groupList:
                settings.USER_GROUPS.append(group['GroupName'])
            settings.ALL_GROUPS = []
            groups = client.list_groups(UserPoolId = settings.COGNITO_USER_POOL_ID) 
            for group in groups['Groups']:
                settings.ALL_GROUPS.append(group["GroupName"])
            #print("all groups " + str(settings.ALL_GROUPS))    
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            msg = ('Authorization token is not valid.')
            raise exceptions.AuthenticationFailed(msg)

        return (user, None) #authentication successful     