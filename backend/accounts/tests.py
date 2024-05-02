from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class TestAuthentication(APITestCase):

    def setUp(self):
        self.user_credentials = {
            "username": "testuser1",
            "email": "testuser@gmail.com",
            "password": "test_password"
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.user_credentials)

    def test_registration(self):
        user_credentials = {
            "username": "testuser2",
            "email": "testuser2@gmail.com",
            "password": "test_password2"
        }
        response = self.client.post(
            reverse('register'),
            data=user_credentials,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_existing_user(self):
        response = self.client.post(
            reverse('register'),
            data=self.user_credentials,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        response = self.client.post(
            reverse('login'),
            data=self.user_credentials,
            format='')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_with_incorrect_credentials(self):
        incorrect_user_credentials = {
            "username": "testuser1",
            "email": "testuser@gmail.com",
            "password": "test_password2"
        }
        with self.assertRaises(ValidationError) as e:
            self.client.post(
                reverse('login'),
                data=incorrect_user_credentials,
                format='')
            self.assertEqual("Such user does not exist", e.exception[0])

    def test_logout_without_token(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_with_token(self):
        self.client.post(
            reverse('login'),
            data=self.user_credentials,
            format='json')
        token = Token.objects.get(user__username="testuser1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_with_token(self):
        self.client.post(
            reverse('login'),
            data=self.user_credentials,
            format='json')
        token = Token.objects.get(user__username="testuser1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(
            reverse('register'),
            data=self.user_credentials,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
