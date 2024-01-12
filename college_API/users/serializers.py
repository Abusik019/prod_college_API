from django.contrib.auth import get_user_model
from rest_framework import serializers


class StudentLoginSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    student_id = serializers.CharField()

    def validate(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        student_id = data.get('student_id')

        try:
            student = get_user_model().objects.get(
                first_name=first_name,
                last_name=last_name,
                student_id=student_id,
                user_type=1
            )
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError('Студент с указанными данными не найден.')

        data['student'] = student
        return data


class TeacherLoginSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    surname = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        first_name = data.get('first_name')
        surname = data.get('surname')
        last_name = data.get('last_name')
        password = data.get('password')

        try:
            teacher = get_user_model().objects.get(
                first_name=first_name,
                surname=surname,
                last_name=last_name,
                password=password,
                user_type=2
            )
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError('Преподаватель с указанными данными не найден.')

        data['teacher'] = teacher
        return data
