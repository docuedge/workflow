from django.test import SimpleTestCase
from django.urls import reverse, resolve
from workflow_vault.signInViews import SignInView
from workflow_vault.views import CreateWorkflow, GetInitiatorDetails,Details
class TestURLs(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('sign-in')
        self.assertEquals(resolve(url).func.view_class, SignInView)
    
    def test_initiate_workflow_url_is_resolved(self):
        url=reverse('create-workflow')
        self.assertEquals(resolve(url).func.view_class,CreateWorkflow)
    
    def test_initiator_details(self):
        url=reverse('get-initiator-details',kwargs={'Id':58})
        self.assertEquals(resolve(url).func.view_class,GetInitiatorDetails)
    
    def test_workflow_review_details(self):
        url=reverse('details', kwargs={'Process_name':'Review'})
        self.assertEquals(resolve(url).func.view_class,Details)
    
    def test_workflow_approval_schema(self):
        url=reverse('details', kwargs={'Process_name':'Approval'})
        self.assertEquals(resolve(url).func.view_class,Details)