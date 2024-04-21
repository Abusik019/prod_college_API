from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class UsersTest(APITestCase):
    """
    Тест пользовательских представлений.
    """
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='test_password1',
            first_name='First1',
            last_name='Last1',
            college_id='123456'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='test_password2',
            first_name='First2',
            last_name='Last2',
            college_id='123457'
        )
        self.token_url = reverse('token_obtain_pair')
        self.token = None

    def get_token(self):
        user_data = {
            'first_name': 'First1',
            'last_name': 'Last1',
            'college_id': '123456'
        }
        token_response = self.client.post(self.token_url, user_data, format='json')
        self.token = token_response.data['access']

    def test_get_user_list(self):
        if not self.token:
            self.get_token()
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('get_users'), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user1.first_name.encode(), response.content)
        self.assertIn(self.user2.first_name.encode(), response.content)
