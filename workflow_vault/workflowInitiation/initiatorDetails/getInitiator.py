import json
import requests
from Workflow_Django.settings import CONSTANT_URL

def getInitiator(id):
    URL = CONSTANT_URL+'queries/processes/instances/'+id+'/variables/instances/Initiator'
    # print(URL)
    header = {'Content-type' : 'application/json'}
    response = requests.get(URL, headers = header).json()
    
    return response