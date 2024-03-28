from rest_framework.permissions import BasePermission

from .models import Exam


class IsTeacherPermission(BasePermission):
    """
    Разрешение, которое проверяет, является ли пользователь учителем.
    """
    def has_permission(self, request, view):
        """
        Метод для проверки разрешения доступа.
        :param request: объект запроса
        :param view: объект представления
        :return: True, если пользователь является учителем, в противном случае False
        """
        return request.user.is_teacher


class GroupPermission(BasePermission):
    """
    Проверка на право студента определенной группы проходить экзамен.
    """
    def has_permission(self, request, view):
        student = request.user.student_profile
        if student:
            exam_id = view.kwargs.get('exam_id')
            exam = Exam.objects.get(id=exam_id)
            return student.group in exam.groups.all()
        return False


class ExamIsEndedPermission(BasePermission):
    """
    Проверка на истечение срока экзамена.
    """
    def has_permission(self, request, view):
        exam_id = view.kwargs.get('exam_id')
        exam = Exam.objects.get(id=exam_id)
        return not exam.ended
