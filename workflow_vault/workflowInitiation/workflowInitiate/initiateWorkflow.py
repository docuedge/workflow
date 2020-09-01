import requests
import json
from fastjsonschema import *
from Workflow_Django.settings import CONSTANT_URL
from workflow_vault.exceptions import WorkflowException
def initiateWorkflow(body):
    # print(type(body))
    correct = False
    for k in body.keys():
        v = body.get(k)
        if v and v.strip():
            correct  = True
        else:
            data = v
            correct = False
            break
    if(correct):
        containerID = body['container-id']
        processID = body['process-id']
        URL = CONSTANT_URL+'containers/'+containerID+'/processes/'+processID+'/instances'
        header = {'Content-type':'application/json'}
        response = requests.post(URL, headers = header, json = body).json()
        return response
    else:
        raise WorkflowException(404, "Validation error",   " Mandatory field is missing")