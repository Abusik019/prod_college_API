from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Student, Teacher
from .serializers import CustomLoginSerializer, UserSerializer, StudentSerializer, TeacherSerializer, \
    UserUpdatePhotoSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_user(serializer.validated_data['college_id'])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# ________________________________________________________________________________________________________


class CurrentUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def user_list(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdatePhotoView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdatePhotoSerializer
    permission_classes = [IsAuthenticated]

# __________________________________________________

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def student_list(request):
    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)


class StudentDetailView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

# __________________________________________________

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def teacher_list(request):
    queryset = Teacher.objects.all()
    serializer = TeacherSerializer(queryset, many=True)
    return Response(serializer.data)


class TeacherDetailView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]


class TeacherUpdateView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_group_ids = request.data.get('group_ids', [])
        current_group_ids = list(instance.group.values_list('id', flat=True))

        groups_to_add = set(new_group_ids) - set(current_group_ids)
        groups_to_remove = set(current_group_ids) - set(new_group_ids)

        for group_id in groups_to_add:
            instance.group.add(group_id)

        for group_id in groups_to_remove:
            instance.group.remove(group_id)

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ________________________________________________________________________________________________________

