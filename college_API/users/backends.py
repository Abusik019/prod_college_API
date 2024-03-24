from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomAuthBackend(ModelBackend):
    """
    Пользовательский аутентификационный бэкенд.
    """
    def authenticate(self, request, first_name=None, last_name=None, college_id=None, **kwargs):
        """
        Переопределение метода аутентификации.
        """
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(
                first_name=first_name,
                last_name=last_name,
                college_id=college_id,
            )
        except UserModel.DoesNotExist:
            return None

        return user
