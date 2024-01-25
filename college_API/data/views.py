from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Group, Subject, Lecture
from .serializers import GroupSerializer, SubjectsSelializers, CreateLectureSerializer, LectureSerializer
from users.models import Student, Teacher
from users.permissions import IsTeacherPermission


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def group_list(request):
    queryset = Group.objects.all()
    serializer = GroupSerializer(queryset, many=True)
    return Response(serializer.data)


class GroupMembersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, group_id):
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response({'detail': 'Группа не найдена'}, status=status.HTTP_404_NOT_FOUND)

        students = Student.objects.filter(group=group)
        teachers = Teacher.objects.filter(group=group)

        student_data = []
        for student in students:
            student_data.append({
                'id': student.id,
                'first_name': student.student.first_name,
                'last_name': student.student.last_name,
                'email': student.student.email,
                'image': student.student.image,
            })

        teacher_data = []
        for teacher in teachers:
            teacher_data.append({
                'id': teacher.id,
                'first_name': teacher.teacher.first_name,
                'last_name': teacher.teacher.last_name,
                'image': teacher.teacher.image,
                'subjects': [subject.name for subject in teacher.subjects.all()],
            })

        return Response({
            'students': student_data,
            'teachers': teacher_data
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def subjects_list(request):
    queryset = Subject.objects.all()
    serializer = SubjectsSelializers(queryset, many=True)
    return Response(serializer.data)


# _________________________________________________________________________________________________________________


class CreateLectureView(CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = CreateLectureSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def perform_create(self, serializer):
        serializer.save(lecturer=self.request.user.teacher_profile)


class TeacherLecturesView(ListAPIView):
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        return Lecture.objects.filter(lecturer__id=teacher_id)


class LectureDetailView(ListAPIView):
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lecture_id = self.kwargs['lecture_id']
        return Lecture.objects.filter(id=lecture_id)


class MyLecturesView(ListAPIView):
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def get_queryset(self):
        teacher = self.request.user.teacher_profile
        return Lecture.objects.filter(lecturer=teacher)


class DeleteLectureView(DestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]


class UpdateLectureView(UpdateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = CreateLectureSerializer
    permission_classes = [IsAuthenticated]
