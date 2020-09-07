from rest_framework.test import APITestCase
from django.urls import reverse
import json

class TestSignInView(APITestCase):

    def setUp(self):
        self.signin = reverse("sign-in")
        return super().setUp()

    def test_SignInView(self):
        data={
            "username":"testuser1",
            "password": "#Password1"
        }
        response = self.client.post("/auth/sign-in",data, format="json")
        
        self.assertEquals(response.status_code,200)