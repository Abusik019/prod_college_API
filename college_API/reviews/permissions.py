from rest_framework.permissions import BasePermission


class IsCommentOwnerOrLectureOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True

        if obj.author == request.user:
            return True

        lecture = obj.lecture
        if request.user.is_teacher:
            if lecture and lecture.lecturer == request.user.teacher_profile:
                return True

        return False
