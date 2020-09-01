import json
import requests
from fastjsonschema import *
from Workflow_Django.settings import CONSTANT_URL

# demo = {'Status': 'String', 'Comment': 'String', 'Initiator': 'String', 'DocumentID': 'String', 'Approver': 'String', 'Document': 'org.jbpm.document.Document', 'Rejection' : 'String'}
# response = requests.get(URL, headers = header).json()
# print(type(response))
# response = response['variables']
#print(fastjsonschema.validate(demo,response))
def getVarDetails(body):
    container_id = body['container-id']
    process_id = body['process-id']
    URL = CONSTANT_URL+'containers/'+container_id+'/processes/definitions/'+process_id+'/variables'
    header= {'Content-type':'application/json'}
    response = requests.get(URL, headers = header).json()
    # response = response['variables']
    print(type(response))
    response['process-variables'] = response.pop('variables')
    # validate_response = validate(response,body)
    # print(validate_response)
    return response