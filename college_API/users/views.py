from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Student, Teacher
from .permissions import IsTeacherPermission
from data.serializers import GroupSerializer
from data.models import Subject

from .serializers import (
    CustomLoginSerializer,
    UserSerializer,
    StudentSerializer,
    TeacherSerializer,
    UserUpdatePhotoSerializer,
    UserUpdateEmailSerializer
)


# ________________________________________________________________________________________________________


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        # Получение сериализатора для обработки запроса
        serializer = self.get_serializer(data=request.data)
        # Проверка валидности данных сериализатором
        serializer.is_valid(raise_exception=True)
        # Получение пользователя на основе переданного идентификатора колледжа
        user = serializer.get_user(serializer.validated_data['college_id'])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# ________________________________________________________________________________________________________


class CurrentUserView(RetrieveAPIView):
    """
    API endpoint для получения текущего пользователя.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def user_list(request):
    """
    API endpoint для получения всех пользователей.
    """
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


class UserDetailView(RetrieveAPIView):
    """
    API endpoint для получения информации о конкретном пользователе.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdatePhotoView(UpdateAPIView):
    '''
    API endpoint для обновления аватара.
    {
        'image': 'test'
    }
    '''
    queryset = User.objects.all()
    serializer_class = UserUpdatePhotoSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateEmailView(UpdateAPIView):
    '''
    API endpoint для обновления email.
    {
        'email': 'test'
    }
    '''
    queryset = User.objects.all()
    serializer_class = UserUpdateEmailSerializer
    permission_classes = [IsAuthenticated]

# ________________________________________________________________________________________________________


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def student_list(request):
    """
    API endpoint для получения всех студентов.
    """
    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)


class StudentDetailView(RetrieveAPIView):
    """
    API endpoint для получения информации о конкретном студенте.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

# ________________________________________________________________________________________________________


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def teacher_list(request):
    """
    API endpoint для получения всех преподов.
    """
    queryset = Teacher.objects.all()
    serializer = TeacherSerializer(queryset, many=True)
    return Response(serializer.data)


class TeacherDetailView(RetrieveAPIView):
    """
    API endpoint для получения информации о конкретном преподе.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]


class TeacherAddGroupsView(UpdateAPIView):
    '''
    API endpoint для обновления групп в которых преподает препод.
    {
        'group_ids': [5, 6]
    }
    '''
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Получение экземпляра преподавателя
        new_group_ids = request.data.get('group_ids', [])  # Получение списка новых идентификаторов групп из запроса
        current_group_ids = list(instance.group.values_list('id', flat=True))  # Получение текущих идентификаторов групп

        groups_to_add = set(new_group_ids) - set(current_group_ids)  # Группы для добавления
        groups_to_remove = set(current_group_ids) - set(new_group_ids)  # Группы для удаления

        for group_id in groups_to_add:
            instance.group.add(group_id)  # Добавление группы преподавателю

        for group_id in groups_to_remove:
            instance.group.remove(group_id)  # Удаление группы у преподавателя

        serializer = self.get_serializer(instance)  # Получение сериализованных данных преподавателя
        return Response(serializer.data, status=status.HTTP_200_OK)  # Возврат ответа с обновленными данными


class TeacherSubjectsView(UpdateAPIView):
    '''
    API endpoint для обновления предметов, которые преподает преподаватель.
    {
        "subject_ids": [1, 2]
    }
    '''
    queryset = Teacher.objects.all()  # Запрос для получения объекта преподавателя
    serializer_class = TeacherSerializer  # Сериализатор для преподавателя
    permission_classes = [IsAuthenticated, IsTeacherPermission]  # Требуемые разрешения для доступа к представлению

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Получение экземпляра преподавателя
        new_subject_ids = request.data.get('subject_ids', [])  # Получение списка новых идентификаторов предметов из запроса
        current_subject_ids = list(instance.subjects.values_list('id', flat=True))  # Получение текущих идентификаторов предметов

        subjects_to_add = set(new_subject_ids) - set(current_subject_ids)  # Предметы для добавления
        subjects_to_remove = set(current_subject_ids) - set(new_subject_ids)  # Предметы для удаления

        for subject_id in subjects_to_add:
            subject = Subject.objects.get(id=subject_id)
            instance.subjects.add(subject)  # Добавление предмета преподавателю

        for subject_id in subjects_to_remove:
            subject = Subject.objects.get(id=subject_id)
            instance.subjects.remove(subject)  # Удаление предмета у преподавателя

        serializer = self.get_serializer(instance)  # Получение сериализованных данных преподавателя
        return Response(serializer.data, status=status.HTTP_200_OK)  # Возврат ответа с обновленными данными


class TeacherGroupsView(APIView):
    """
    API endpoint для получения групп препода.
    """
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def get(self, request, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(teacher=request.user)  # Получение экземпляра преподавателя по текущему пользователю
        except Teacher.DoesNotExist:
            return Response({"error": "Преподаватель не найден."}, status=status.HTTP_404_NOT_FOUND)  # Возврат ошибки, если преподаватель не найден

        groups = teacher.group.all()  # Получение всех групп, преподаваемых преподавателем
        serializer = GroupSerializer(groups, many=True)  # Сериализация списка групп
        return Response(serializer.data, status=status.HTTP_200_OK)  # Возврат данных групп с успешным статусом


class MyGroupView(ListAPIView):
    """
    API endpoint для получения группы студента.
    """
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = self.request.user.student_profile  # Получение профиля студента текущего пользователя
        if student.group:
            return [student.group]  # Возвращаем список группы студента, если она существует
        else:
            return []  # Возвращаем пустой список, если группа не указана


class CreateUser(CreateAPIView):
    """
    API endpoint для создания пользователя.
    """
    queryset = User.objects.all()
    permission_classes = [IsAdminUser,]
    serializer_class = UserSerializer


# ________________________________________________________________________________________________________

