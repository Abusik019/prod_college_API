from rest_framework.permissions import BasePermission


class IsTeacherPermission(BasePermission):
    """
    Пользовательское разрешение для проверки, является ли пользователь учителем.
    """

    def has_permission(self, request, view):
        """
        Проверяет, имеет ли пользователь разрешение на доступ к представлению.
        Возвращает True, если пользователь является учителем, иначе False.
        """
        return request.user.is_teacher
