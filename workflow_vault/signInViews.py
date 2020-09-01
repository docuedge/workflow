from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import json
from workflow_vault.signIn.cognito import handler as CognitoLogin
from workflow_vault.signIn.refreshToken import handler as RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.conf import settings

# Create your views here.
class SignInView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        resp: {}
        body = json.loads(request.body)
        resp = CognitoLogin(body)
        return JsonResponse(resp, safe=False)

class RefreshTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        resp: {}
        body = json.loads(request.body)
        resp = RefreshToken(body)
        return JsonResponse(resp, safe=False)

# class UserGroupsView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         resp = settings.USER_GROUPS
#         return JsonResponse(resp, safe=False)

# class AllUserGroupsView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         resp = settings.ALL_GROUPS
#         return JsonResponse(resp, safe=False)
