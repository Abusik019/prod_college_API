from django.urls import path
from .views import user_list, student_list, teacher_list, UserDetailView, StudentDetailView, UserUpdatePhotoView, \
    TeacherDetailView, CurrentUserView, TeacherAddGroupsView, TeacherGroupsView, TeacherSubjectsView


urlpatterns = [
    path('get_users', user_list, name='get_users'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user_photo_update/<int:pk>', UserUpdatePhotoView.as_view(), name='user_photo_update'),
    path('current_user', CurrentUserView.as_view(), name='current_user'),

    path('get_students', student_list, name='get_students'),
    path('student_detail/<int:pk>', StudentDetailView.as_view(), name='student_detail'),

    path('get_teachers', teacher_list, name='get_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='get_teacher'),
    path('teacher_update/<int:pk>', TeacherAddGroupsView.as_view(), name='teacher_update'),
    path('add_subjects/<int:pk>', TeacherSubjectsView.as_view(), name='add_subjects'),
    path('my_groups', TeacherGroupsView.as_view(), name='my_groups'),
]

