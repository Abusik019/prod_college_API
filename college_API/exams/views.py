from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Exam, ExamResult
from .permissions import IsTeacherPermission, GroupPermission, ExamIsEndedPermission
from .serializers import ExamSerializer, ExamResultSerializer
from .email_senders import send_exam_notification, send_result_notification
from .utils import calculate_exam_score


class CreateExamView(CreateAPIView):
    """
    API endpoint для создания экзамена.
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def perform_create(self, serializer):
        """
        Переопределение метода perform_create для отправки уведомления после создания экзамена.
        """
        exam = serializer.save()
        send_exam_notification(instance=exam, created=True)


class UpdateExamView(UpdateAPIView):
    """
    API endpoint для обновления экзамена.
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]


class DestroyExamView(DestroyAPIView):
    """
    API endpoint для удаления экзамена.
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]


class TeacherExamsView(ListAPIView):
    """
    API endpoint для получения списка экзаменов учителя.
    """
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'teacher_profile'):
            return Exam.objects.filter(author=user.teacher_profile)
        return Exam.objects.none()


class StudentExamsView(ListAPIView):
    """
    API endpoint для получения списка экзаменов студента.
    """
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'student_profile'):
            return Exam.objects.filter(groups=user.student_profile.group)
        return Exam.objects.none()


class StartExam(ListAPIView):
    """
    API endpoint для просмотра экзаменов препода.
    """
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        teacher_id = self.kwargs['pk']
        return Exam.objects.filter(author=teacher_id)


# class StartExam()


class PassExamView(APIView):
    '''
    API endpoint для прохождения экзамена студентом.
    {
        "answers": [
            {"question_id": 1, "selected_answer_id": 1}
        ]
    }
    '''
    permission_classes = [IsAuthenticated, GroupPermission, ExamIsEndedPermission]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        student = user.student_profile
        exam_id = self.kwargs.get('exam_id')

        answers_data = request.data.get('answers', [])
        score = calculate_exam_score(answers_data)
        serializer = ExamResultSerializer(data={'exam': exam_id, 'student': student.id, 'score': score})
        if serializer.is_valid():
            result = serializer.save()
            send_result_notification(instance=result, created=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentResultsView(ListAPIView):
    """
    API endpoint для просмотра результатов экзаменов студента.
    """

    serializer_class = ExamResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = self.request.user.student_profile
        return ExamResult.objects.filter(student=student)


class TeacherResultsView(ListAPIView):
    """
    API endpoint для просмотра результатов экзаменов преподавателя.
    """

    serializer_class = ExamResultSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def get_queryset(self):
        teacher = self.request.user.teacher_profile
        exams = Exam.objects.filter(author=teacher)
        return ExamResult.objects.filter(exam__in=exams)
