import random

import factory
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

from data.models import Group, Facult, Course, PodGroup, Subject


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
    is_teacher = False
    is_staff = False
    is_superuser = False


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    @factory.lazy_attribute
    def facult(self):
        return Facult.objects.create(name='ИСИП')

    @factory.lazy_attribute
    def course(self):
        return Course.objects.create(name=f'{random.randint(1, 10)}')

    @factory.lazy_attribute
    def podgroup(self):
        return PodGroup.objects.create(name=f'{random.randint(1, 10)}')


# _________________________________________________________________________________________________________


class UsersBaseTest(APITestCase):
    """
    Базовый класс для тестов пользовательских представлений.
    """
    def setUp(self):
        self.group = GroupFactory(
            facult=GroupFactory.facult,
            course=GroupFactory.course,
            podgroup=GroupFactory.podgroup
        )

        self.user = UserFactory()

        self.token_url = reverse('token_obtain_pair')
        self.token = None

    def get_token(self, user):
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'college_id': user.college_id
        }
        token_response = self.client.post(self.token_url, user_data, format='json')
        self.token = token_response.data['access']


# _________________________________________________________________________________________________________


class UsersTest(UsersBaseTest):
    """
    Тесты пользовательских представлений.
    """
    def test_get_user_list(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('get_users'), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user.first_name.encode(), response.content)

    def test_update_photo_user(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {'image': 'test'}
        response = self.client.put(
            reverse('user_photo_update', kwargs={'pk': self.user.pk}),
            headers=headers, data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['image'], 'test')

    def test_update_email_user(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {'email': 'test@gmail.com'}
        response = self.client.put(
            reverse('user_email_update', kwargs={'pk': self.user.pk}),
            headers=headers, data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@gmail.com')

    def test_current_user(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('current_user'), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.user.id)


class StudentTest(UsersBaseTest):
    """
    Тесты студенческих представлений.
    """
    def setUp(self):
        super().setUp()
        self.user.student_profile.group = self.group
        self.user.student_profile.save()

    def test_user_detail(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('user_detail', kwargs={'pk': self.user.pk}), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user.first_name.encode(), response.content)
        self.assertIn(self.user.last_name.encode(), response.content)
        self.assertIn(self.user.email.encode(), response.content)
        self.assertIn(self.user.image.encode(), response.content)
        self.assertIn('is_teacher', response.data)
        self.assertEqual(self.user.student_profile.group.course.name, response.data['group']['course_name'])
        self.assertEqual(self.user.student_profile.group.facult.name, response.data['group']['facult_name'])
        self.assertEqual(self.user.student_profile.group.podgroup.name, response.data['group']['podgroup_name'])

    def test_my_group(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('my_group'), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], self.user.student_profile.group.id)
        self.assertEqual(response.data[0]['facult_name'], self.user.student_profile.group.facult.name)
        self.assertEqual(response.data[0]['course_name'], self.user.student_profile.group.course.name)
        self.assertEqual(response.data[0]['podgroup_name'], self.user.student_profile.group.podgroup.name)

    def test_get_students(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('get_students'), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['student']['first_name'], self.user.first_name)
        self.assertEqual(response.data[0]['student']['last_name'], self.user.last_name)

    def test_student_detail(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('student_detail', kwargs={'pk': self.user.pk}), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['student']['first_name'], self.user.first_name)
        self.assertEqual(response.data['student']['last_name'], self.user.last_name)
        self.assertEqual(response.data['group']['facult_name'], self.user.student_profile.group.facult.name)
        self.assertEqual(response.data['group']['course_name'], self.user.student_profile.group.course.name)
        self.assertEqual(response.data['group']['podgroup_name'], self.user.student_profile.group.podgroup.name)


class TeacherTest(UsersBaseTest):
    """
    Тесты учительских представлений.
    """
    def setUp(self):
        super().setUp()
        self.teacher = UserFactory(is_teacher=True)

        self.subject = Subject.objects.create(name='Алгоритмизация')

        self.teacher.teacher_profile.group.set([self.group])
        self.teacher.teacher_profile.subjects.set([self.subject])

        self.group2 = GroupFactory(
            facult=GroupFactory.facult,
            course=GroupFactory.course,
            podgroup=GroupFactory.podgroup
        )

    def test_get_teachers(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(reverse('get_teacher'), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['teacher']['first_name'], self.teacher.first_name)
        self.assertEqual(response.data[0]['subjects'][0], self.teacher.teacher_profile.subjects.first().name)
        self.assertEqual(response.data[0]['group'][0]['facult_name'], self.teacher.teacher_profile.group.first().facult.name)

    def test_teacher_detail(self):
        if not self.token:
            self.get_token(self.user)
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(
            reverse('teacher_detail', kwargs={'pk': self.teacher.teacher_profile.id}),
            headers=headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['teacher']['first_name'], self.teacher.first_name)
        self.assertEqual(response.data['subjects'][0], self.teacher.teacher_profile.subjects.first().name)
        self.assertEqual(response.data['group'][0]['facult_name'], self.teacher.teacher_profile.group.first().facult.name)

    def test_update_teacher(self):
        if not self.token:
            self.get_token(self.teacher)
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {"group_ids": [self.group2.id]}
        response = self.client.put(
            reverse('teacher_update', kwargs={'pk': self.teacher.teacher_profile.id}),
            headers=headers, data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
