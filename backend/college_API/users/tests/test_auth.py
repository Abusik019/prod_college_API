from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class CustomTokenObtainPairViewTest(APITestCase):
    """
    Тест авторизации по JWT токенам.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            first_name='Test',
            last_name='User',
            college_id='123456'
        )
        self.url = reverse('token_obtain_pair')
        self.refresh_token = None

    def test_token_obtain_pair(self):
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'college_id': '123456'
        }
        response = self.client.post(self.url, data, format='json')
        self.refresh_token = response.data['refresh']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_refresh_token(self):
        if not self.refresh_token:
            self.test_token_obtain_pair()
        data = {'refresh': self.refresh_token}
        response = self.client.post(reverse('token_refresh'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_token_obtain_pair_invalid_credentials(self):
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'college_id': 'invalid_id'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
