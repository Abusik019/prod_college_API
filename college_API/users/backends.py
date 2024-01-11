from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class TeacherAuthBackend(ModelBackend):
    def authenticate(self, request, first_name=None, surname=None, last_name=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            teacher = UserModel.objects.get(
                first_name=first_name,
                surname=surname,
                last_name=last_name,
                password=password,
                user_type=2
            )
        except UserModel.DoesNotExist:
            return None

        return teacher if teacher.check_password(password) else None


class StudentAuthBackend(ModelBackend):
    def authenticate(self, request, first_name=None, last_name=None, student_id=None, **kwargs):
        UserModel = get_user_model()
        try:
            student = UserModel.objects.get(
                first_name=first_name,
                last_name=last_name,
                student_id=student_id,
                user_type=1
            )
        except UserModel.DoesNotExist:
            return None

        return student

