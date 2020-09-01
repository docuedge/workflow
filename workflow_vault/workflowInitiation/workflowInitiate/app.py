from .initiateWorkflow import *

def startWorkflow(event):
    body = json.loads(event.body)
    response = initiateWorkflow(body)
    return response
