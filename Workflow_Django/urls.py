"""Workflow_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workflow_vault.views import *
from workflow_vault.signInViews import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('workflow/getIDs/', GetWorkflow.as_view(), name = "get-workflow"),
    path('wfservice/wfinitiate/', CreateWorkflow.as_view(), name= "create-workflow"),
    path('workflow/getInitiator/<int:Id>', GetInitiatorDetails.as_view() , name="get-initiator-details"),
    path('wfservice/<str:Process_name>/wfinfo', Details.as_view(), name = "details"),
    path('auth/sign-in', SignInView.as_view(), name='sign-in'), 
    path('auth/refresh', RefreshTokenView.as_view(), name='refresh-token'),
    # path('usergroups/user', UserGroupsView.as_view(), name='user-groups'),
    # path('usergroups/all', AllUserGroupsView.as_view(), name='all-user-groups'),
   
]