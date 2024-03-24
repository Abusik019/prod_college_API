from rest_framework.permissions import BasePermission


class IsCommentOwnerOrLectureOwnerOrAdmin(BasePermission):
    """
    Пользователь может редактировать или удалять комментарий, если он:
    - администратор
    - владелец комментария
    - преподаватель, который является автором лекции, под которой опубликован комментарий
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True  # Администратор имеет все права.

        if obj.author == request.user:
            return True  # Владелец комментария может редактировать или удалять его.

        lecture = obj.lecture
        if request.user.is_teacher:
            if lecture and lecture.lecturer == request.user.teacher_profile:
                return True  # Преподаватель, автор лекции, может редактировать или удалять комментарии под своей лекцией.

        return False  # В остальных случаях возвращаем False.
