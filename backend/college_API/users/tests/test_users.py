import factory
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

from data.models import Group, Facult, Course, PodGroup


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    first_name = 'First'
    last_name = 'Last'
    college_id = factory.Sequence(lambda n: f'12345{n}')
    image = factory.Sequence(lambda n: f'img/{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')


class UsersTest(APITestCase):
    """
    Тест пользовательских представлений.
    """
    def setUp(self):
        self.facult = Facult.objects.create(name='ИСИП')
        self.course = Course.objects.create(name='3')
        self.podgroup = PodGroup.objects.create(name='1')
        self.group = Group.objects.create(facult=self.facult, course=self.course, podgroup=self.podgroup)

        self.user1 = UserFactory()
        self.user2 = UserFactory()

        self.user1.student_profile.group = self.group
        self.user1.student_profile.save()

        self.token_url = reverse('token_obtain_pair')
        self.token = None

    def get_token(self):
        user_data = {
            'first_name': self.user1.first_name,
            'last_name': self.user1.last_name,
            'college_id': self.user1.college_id
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

    def test_user_detail(self):
        if not self.token:
            self.get_token()
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('user_detail', kwargs={'pk': self.user1.pk}), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user1.first_name.encode(), response.content)
        self.assertIn(self.user1.last_name.encode(), response.content)
        self.assertIn(self.user1.email.encode(), response.content)
        self.assertIn(self.user1.image.encode(), response.content)
        self.assertIn('is_teacher', response.data)
        self.assertEqual(self.user1.student_profile.group.course.name, response.data['group']['course_name'])
        self.assertEqual(self.user1.student_profile.group.facult.name, response.data['group']['facult_name'])
        self.assertEqual(self.user1.student_profile.group.podgroup.name, response.data['group']['podgroup_name'])

    def test_update_photo_user(self):
        if not self.token:
            self.get_token()
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {'image': 'test'}
        response = self.client.put(
            reverse('user_photo_update', kwargs={'pk': self.user1.pk}),
            headers=headers, data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['image'], 'test')

    def test_update_email_user(self):
        if not self.token:
            self.get_token()
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {'email': 'test@gmail.com'}
        response = self.client.put(
            reverse('user_email_update', kwargs={'pk': self.user1.pk}),
            headers=headers, data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@gmail.com')

    def test_current_user(self):
        if not self.token:
            self.get_token()
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('current_user'), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.user1.id)
