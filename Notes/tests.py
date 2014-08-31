from json import loads
from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status


class UserAPITestCase(APITestCase):
    user1 = {'username': 'test-user-1', 'password': 'test-pass-1'}
    user2 = {'username': 'test-user-2', 'password': 'test-pass-2'}

    def get_user(self, cred):
        return User.object.get(username=cred['username'])

    def get_token(self, cred):
        data = {
            'grant_type': 'password',
            'username': cred['username'],
            'password': cred['password'],
            'client_id': cred['username']
        }

        response = self.client.post('/oauth2/access_token', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = loads(response.content)

        self.assertTrue('access_token' in response_data)
        token = response_data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ token)


class NotesTest(UserAPITestCase):
    def create_note(self):
        data = {'text': 'Test note 1'}
        return self.client.post('/notes/', data)

    def test_create_note(self):
        self.get_token(self.user1)
        response = self.create_note()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/todos/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 1)
        self.assertEqual(response.data[0]['text'], 'Test note 1')
