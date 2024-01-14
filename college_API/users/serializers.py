from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Student, Teacher


class CustomLoginSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    college_id = serializers.CharField()

    def validate(self, attrs):
        data = super().validate(attrs)

        if 'first_name' not in attrs or not attrs['first_name']:
            raise serializers.ValidationError({'first_name': 'Это обязательное поле.'})

        if 'last_name' not in attrs or not attrs['last_name']:
            raise serializers.ValidationError({'last_name': 'Это обязательное поле.'})

        if 'college_id' not in attrs or not attrs['college_id']:
            raise serializers.ValidationError({'college_id': 'Это обязательное поле.'})

        try:
            user = User.objects.get(
                first_name=attrs['first_name'],
                last_name=attrs['last_name'],
                college_id=attrs['college_id']
            )
        except User.DoesNotExist:
            raise serializers.ValidationError({'Error': 'Пользователь не найден.'})

        data['access'] = str(RefreshToken.for_user(user).access_token)
        data['refresh'] = str(RefreshToken.for_user(user))
        return data

    def get_user(self, college_id):
        try:
            return User.objects.get(college_id=college_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({'college_id': 'Пользователь не найден.'})

# ______________________________________________________________________________________________________________

class UserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'image', 'is_teacher', 'user']


class StudentSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField('get_user_info')

    def get_user_info(self, obj):
        user = obj.student
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'image': user.image,
        }
        return user_data

    class Meta:
        model = Student
        fields = ['id', 'student', 'group']


class TeacherSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField('get_user_info')

    def get_user_info(self, obj):
        user = obj.teacher
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'image': user.image,
        }
        return user_data

    class Meta:
        model = Teacher
        fields = ['id', 'teacher', 'group']


class TeacherUpdateSerializer(serializers.Serializer):
    course = serializers.ListField(child=serializers.IntegerField(), required=False)
    group = serializers.ListField(child=serializers.IntegerField(), required=False)
    facult = serializers.ListField(child=serializers.IntegerField(), required=False)