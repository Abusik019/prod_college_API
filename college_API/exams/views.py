from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
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
           send_exam_notification(instance=exam, created=True)


class UpdateExamView(UpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]


class DestroyExamView(DestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]


class TeacherExamsView(ListAPIView):
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'teacher_profile'):
            return Exam.objects.filter(author=user.teacher_profile)
        return Exam.objects.none()
