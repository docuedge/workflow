
from .getInitiator import *
def getInitiatorName(event):
    body = event.body
    id = str(body['Id'])
    response = getInitiator(id)
    return response
