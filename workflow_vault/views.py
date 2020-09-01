from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from workflow_vault.configuration import *
from workflow_vault.workflowInitiation.getProcessAndContainers.app import getIds as getWorkflowDetails
from workflow_vault.workflowInitiation.workflowInitiate.app import startWorkflow
from workflow_vault.workflowInitiation.schemaDetails.app import getProcessDetails
from workflow_vault.workflowInitiation.initiatorDetails.app import getInitiatorName
from workflow_vault.exceptions import WorkflowException
from workflow_vault.configuration import *

# Create your views here.

class GetWorkflow(APIView):
    def get(self, request):
        result = getWorkflowDetails(request)
        return JsonResponse(result, safe = False)


class CreateWorkflow(APIView):
    def post(self,request ):
        result= startWorkflow(request)
        return JsonResponse(result, safe=False)


class GetInitiatorDetails(APIView):
    def get(self, request, Id):
        # body = json.loads(request.body)
        # print(type(body))
        request.body = {"Id": Id}
        result = getInitiatorName(request)
        return JsonResponse(result , safe = False)





class Details(APIView):
    def get(self,request, Process_name):
        resp = PROCESS_NAME
        process_name = Process_name
        if process_name in resp :
            if process_name==resp[0]:
                container_id= REVIEW_CONTAINER_ID
                process_id = REVIEW_PROCESS_ID
                request.body = {"container-id":container_id, "process-id":process_id}
            elif process_name==resp[1]:
                container_id= APPROVAL_CONTAINER_ID
                process_id = APPROVAL_PROCESS_ID
                request.body = {"container-id":container_id, "process-id":process_id}
            result = getProcessDetails(request)
        else:
          
            result = "Please enter a valid process-type"
        return JsonResponse(result, safe = False)
