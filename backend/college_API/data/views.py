from django.views.decorators.cache import cache_page
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Group, Subject, Lecture
from .serializers import GroupSerializer, SubjectsSelializers, CreateLectureSerializer, LectureSerializer, GroupMembers
from users.permissions import IsTeacherPermission


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def group_list(request):
    """
    Функция возвращающая список групп колледжа.
    """
    queryset = Group.objects.all()
    serializer = GroupSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def subjects_list(request):
    """
    Функция возвращающая список дисциплин.
    """
    queryset = Subject.objects.all()
    serializer = SubjectsSelializers(queryset, many=True)
    return Response(serializer.data)


class GroupMembersView(RetrieveAPIView):
    """
    Представление возвращающее всех членов определенной группы.
    """
    queryset = Group.objects.all()
    serializer_class = GroupMembers
    permission_classes = [IsAuthenticated,]


# _________________________________________________________________________________________________________________


class CreateLectureView(CreateAPIView):
    """
    Представление для создания лекции учителем.
    """
    queryset = Lecture.objects.all()
    serializer_class = CreateLectureSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]


class TeacherLecturesView(ListAPIView):
    """
    Представление возвращающее все лекции определенного препода.
    """
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        return Lecture.objects.filter(lecturer__id=teacher_id)  # Фильтрация лекций по переданному id препода


class LectureDetailView(ListAPIView):
    """
    Представление для просмотра лекции.
    """
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lecture_id = self.kwargs['lecture_id']
        return Lecture.objects.filter(id=lecture_id)    # Фильтрация лекции по переданному id.


class MyLecturesView(ListAPIView):
    """
    Представление для просмотра преподом его лекций.
    """
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]

    def get_queryset(self):
        teacher = self.request.user.teacher_profile
        return Lecture.objects.filter(lecturer=teacher)


class DeleteLectureView(DestroyAPIView):
    """
    Представление для удаления лекции.
    """
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated, IsTeacherPermission]


class UpdateLectureView(UpdateAPIView):
    """
    Представление для изменения лекции.
    """
    queryset = Lecture.objects.all()
    serializer_class = CreateLectureSerializer
    permission_classes = [IsAuthenticated]
