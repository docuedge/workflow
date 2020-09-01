import requests
import json
from Workflow_Django.settings import CONSTANT_URL
def getDetails():
    URL = CONSTANT_URL+'containers/business-application-kjar/processes'
    headers = {'Content-type':'application/json'}
    request = requests.get(URL, headers=headers).json()
    return request