from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Exam, Question, Answer
from .permissions import IsTeacherPermission
from .serializers import ExamSerializer
from users.models import Student


class CreateExam(CreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def perform_create(self, serializer):
        exam = serializer.save(author=self.request.user.teacher_profile)
        self.send_exam_notification(exam)

    def send_exam_notification(self, exam):
        students = Student.objects.filter(group__in=exam.groups.all())
        subject = f"Новый экзамен: {exam.title}"
        message = f"На сайте добавлен новый экзамен: {exam.title}. Пройдите тестирование."
        from_email = "xaclafun1991@gmail.com"
        recipient_list = [student.student.email for student in students]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
