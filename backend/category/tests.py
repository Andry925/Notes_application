from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Category


class CategoryTestCase(APITestCase):

    def setUp(self):
        self.user_credentials = {
            'username': 'tester123',
            'email': 'test@gmail.com',
            'password': 'panel2004'
        }
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            **self.user_credentials)
        self.category_data = {
            'owner': self.user.id,
            'name': 'Test Category',
            'color': '#FF6C6DFF',
        }
        self.category = Category.objects.create(
            owner=self.user, name='Test Category', color='#FF6C6DFF')
        self.client.post(reverse('login'), data=self.user_credentials)
        self.token = Token.objects.get(user__username="tester123")

    def test_retrieve_categories(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        new_auction_data = {
            'owner': self.user.id,
            'name': 'Test Category2',
            'color': '#FF6C6DFF',

        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(
            reverse('categories'),
            data=new_auction_data,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_category_without_token(self):
        response = self.client.post(
            reverse('categories'),
            data=self.category_data,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_already_existing_category(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(
            reverse('categories'),
            data=self.category_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
