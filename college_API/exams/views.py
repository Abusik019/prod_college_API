from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Exam
from .permissions import IsTeacherPermission
from .serializers import ExamSerializer
from .email_senders import send_exam_notification


class CreateExamView(CreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def perform_create(self, serializer):
           exam = serializer.save()
           send_exam_notification(sender=Exam, instance=exam, created=True)
