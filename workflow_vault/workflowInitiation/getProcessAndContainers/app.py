from .getDetails import *


def getIds(event):
    body = event.body
    response = getDetails()
    return response
