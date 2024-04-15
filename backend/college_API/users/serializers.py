from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Student, Teacher

from data.serializers import GroupSerializer


class CustomLoginSerializer(serializers.Serializer):
    """
    Сериализатор для пользовательской аутентификации и генерации токенов доступа.
    """

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    college_id = serializers.CharField()

    def validate(self, attrs):
        """
        Проверяет правильность введенных данных и генерирует токены доступа.
        """
        data = super().validate(attrs)

        # Проверка наличия и заполненности имени пользователя
        if 'first_name' not in attrs or not attrs['first_name']:
            raise serializers.ValidationError({'first_name': 'Это обязательное поле.'})

        # Проверка наличия и заполненности фамилии пользователя
        if 'last_name' not in attrs or not attrs['last_name']:
            raise serializers.ValidationError({'last_name': 'Это обязательное поле.'})

        # Проверка наличия и заполненности идентификатора колледжа пользователя
        if 'college_id' not in attrs or not attrs['college_id']:
            raise serializers.ValidationError({'college_id': 'Это обязательное поле.'})

        # Поиск пользователя по указанным данным
        try:
            user = User.objects.get(
                first_name=attrs['first_name'],
                last_name=attrs['last_name'],
                college_id=attrs['college_id']
            )
        except User.DoesNotExist:
            raise serializers.ValidationError({'Error': 'Пользователь не найден.'})

        # Генерация токенов доступа
        data['access'] = str(RefreshToken.for_user(user).access_token)
        data['refresh'] = str(RefreshToken.for_user(user))
        return data

    def get_user(self, college_id):
        """
        Получает пользователя по идентификатору колледжа.
        """
        try:
            return User.objects.get(college_id=college_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({'college_id': 'Пользователь не найден.'})

# ______________________________________________________________________________________________________________


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя.
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    group = serializers.SerializerMethodField('get_group')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'image', 'is_teacher', 'user', 'group']

    def get_group(self, obj):
        """
        Возвращает группу пользователя.
        """
        # Если пользователь препод, то через вложенный сериализатор групп возвращается все группы препода
        if obj.is_teacher:
            return GroupSerializer(obj.teacher_profile.group.all(), many=True).data
        # Если пользователь студент, то через вложенный сериализатор групп возвращается его группа
        elif hasattr(obj, 'student_profile') and obj.student_profile.group:
            return GroupSerializer(obj.student_profile.group).data
        return None

    def create(self, validated_data):
        """
        Переопределение метода создания пользователя.
        """
        user = validated_data.pop('user')
        instance = super().create(validated_data)
        return instance


class UserUpdatePhotoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления фотографии пользователя.
    """
    class Meta:
        model = User
        fields = ['image']


class UserUpdateEmailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления адреса электронной почты пользователя.
    """
    class Meta:
        model = User
        fields = ['email']


# _____________________________________________________


class StudentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для студента.
    """
    student = serializers.SerializerMethodField('get_user_info')
    group = serializers.SerializerMethodField('get_group')

    def get_user_info(self, obj):
        """
        Получение информации о пользователе.
        """
        user = obj.student
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'image': user.image,
        }
        return user_data

    def get_group(self, obj):
        """
        Получение информации о группе студента.
        """
        return GroupSerializer(obj.group).data if obj.group else None

    class Meta:
        model = Student
        fields = ['id', 'student', 'group']


# _____________________________________________________


class TeacherSerializer(serializers.ModelSerializer):
    """
    Сериализатор для преподавателя.
    """
    teacher = serializers.SerializerMethodField('get_user_info')
    group = serializers.SerializerMethodField('get_group')
    subjects = serializers.SerializerMethodField('get_subjects_names')

    def get_user_info(self, obj):
        """
        Получение информации о пользователе.
        """
        user = obj.teacher
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'image': user.image,
        }
        return user_data

    def get_group(self, obj):
        """
        Получение информации о группах, в которых преподает преподаватель.
        """
        return GroupSerializer(obj.group.all(), many=True).data

    def get_subjects_names(self, obj):
        """
        Получение названий предметов, которые преподает преподаватель.
        """
        return [subject.name for subject in obj.subjects.all()]

    class Meta:
        model = Teacher
        fields = ['id', 'teacher', 'subjects', 'group']


# ______________________________________________________________________________________________________

