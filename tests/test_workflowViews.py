
import json
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from django.urls import reverse,resolve



class TestWorkflowInititation(APITestCase):

    def setUp(self):
        self.createURL= reverse("create-workflow")
        user = 'Garima'
        self.client.force_authenticate(user=user, token=None)
        return super().setUp()

    def test_WorkflowInitiate(self):
        data={ 
            "Approver" : "Garima",
            "Initiator":"Samuel",
            "DocumentID": "1000",
            "Status":"Review",
            "container-id" : "business-application-kjar-1_0-SNAPSHOT",
            "process-id" : "business-application-kjar.vault-doc-approval"
 
        }

        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post("/wfservice/wfinitiate/",data, format="json")
        self.assertEquals(response.status_code,200)

class TestReviewSchemaDetails(APITestCase):
    def setUp(self):

        self.schemaURL=reverse("details",kwargs={'Process_name':'Review'})
        user='Garima'
        self.client.force_authenticate(user=user)
        return super().setUp()
    def test_ReviewSchemaDetails(self):
        
        response = self.client.get('/wfservice/<str:Process_name>/wfinfo',{'Process_name':'Review'}, format="json")
        self.assertEquals(response.status_code,200)


class TestApprovalSchemaDetails(APITestCase):
    def setUp(self):
        self.schemaURL=reverse("details",kwargs={'Process_name':'Approval'})
        user='Garima'
        self.client.force_authenticate(user=user)
        return super().setUp()
    def test_ApprovalSchemaDetails(self):
        
        response = self.client.get('/wfservice/<str:Process_name>/wfinfo',{'Process_name':'Approval'}, format="json")
        
        self.assertEquals(response.status_code,200)
        

class TestInitiatorRetrieval(APITestCase):
    def setUp(self):
        user='Garima'
        self.client.force_authenticate(user=user)
        return super().setUp()
    def test_GetInitiator(self):
        self.getURL = reverse("get-initiator-details", kwargs={'Id':851})
        
        response = self.client.get(self.getURL,format= 'json')
        
        self.assertEquals(response.status_code, 200)
