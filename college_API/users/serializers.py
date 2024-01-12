from django.contrib.auth import get_user_model
from rest_framework import serializers


class CustomLoginSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    college_id = serializers.CharField()

    def validate(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        college_id = data.get('college_id')

        try:
            user = get_user_model().objects.get(
                first_name=first_name,
                last_name=last_name,
                college_id=college_id,
            )
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError('Пользователь с указанными данными не найден.')

        data['user'] = user
        return data
