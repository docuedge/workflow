import json 

class WorkflowException(Exception):
    def __init__(self,status_code,type,message):
        self.status_code = status_code
        self.type = type
        self.message = message

    def __str__(self):
        error = {"status" : self.status_code,
                 "type" : self.type,  
                 "message" : self.message}
        return(json.dumps(error))