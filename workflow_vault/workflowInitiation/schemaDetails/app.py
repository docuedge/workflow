from .getVarDetails import *
import json

def getProcessDetails(event):
    body = event.body
    response = getVarDetails(body)
    return response