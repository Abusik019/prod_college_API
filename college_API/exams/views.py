from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Exam
from .permissions import IsTeacherPermission
from .serializers import ExamSerializer


class CreateExamView(CreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]
