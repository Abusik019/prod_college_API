from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Exam, ExamResult
from .permissions import IsTeacherPermission
from .serializers import ExamSerializer, ExamResultSerializer
from .email_senders import send_exam_notification
from .utils import calculate_exam_score


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


class StudentExamsView(ListAPIView):
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'student_profile'):
            return Exam.objects.filter(groups=user.student_profile.group)
        return Exam.objects.none()


class PassExamView(APIView):
    '''
    {
        "answers": [
            {"question_id": 1, "selected_answer_id": 1}
        ]
    }
    '''
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        student = user.student_profile
        exam_id = self.kwargs.get('exam_id')

        answers_data = request.data.get('answers', [])
        score = calculate_exam_score(answers_data)
        serializer = ExamResultSerializer(data={'exam': exam_id, 'student': student.id, 'score': score})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentResultsView(ListAPIView):
    serializer_class = ExamResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = self.request.user.student_profile
        return ExamResult.objects.filter(student=student)


class TeacherResultsView(ListAPIView):
    serializer_class = ExamResultSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def get_queryset(self):
        teacher = self.request.user.teacher_profile
        exams = Exam.objects.filter(author=teacher)
        return ExamResult.objects.filter(exam__in=exams)
