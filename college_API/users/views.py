from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentLoginSerializer, TeacherLoginSerializer


class CustomStudentTokenObtainPairView(TokenObtainPairView):
    serializer_class = StudentLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class CustomTeacherTokenObtainPairView(TokenObtainPairView):
    serializer_class = TeacherLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

