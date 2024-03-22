from rest_framework.permissions import BasePermission


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
