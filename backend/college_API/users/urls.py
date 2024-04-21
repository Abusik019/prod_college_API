from django.urls import path
from .views import (
    user_list, student_list,
    teacher_list, UserDetailView,
    StudentDetailView, UserUpdatePhotoView,
    TeacherDetailView, CurrentUserView,
    TeacherAddGroupsView, TeacherGroupsView,
    TeacherSubjectsView, MyGroupView,
    UserUpdateEmailView, CreateUser
)


urlpatterns = [
    path('get_users', user_list, name='get_users'),    # Получение всех пользователей
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='user_detail'),     # Информация о пользователе
    path('user_photo_update/<int:pk>', UserUpdatePhotoView.as_view(), name='user_photo_update'),    # Обновление аватара
    path('user_email_update/<int:pk>', UserUpdateEmailView.as_view(), name='user_email_update'),    # Обновление email
    path('current_user', CurrentUserView.as_view(), name='current_user'),   # Текущий пользователь
    path('my_group', MyGroupView.as_view(), name='my_group'),   # Просмотр группы студента

    path('get_students', student_list, name='get_students'),    # Получение всех студентов
    path('student_detail/<int:pk>', StudentDetailView.as_view(), name='student_detail'),    # Информация о студенте

    path('get_teachers', teacher_list, name='get_teacher'),     # Получение всех преподов
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='get_teacher'),   # Информация о преподе
    path('teacher_update/<int:pk>', TeacherAddGroupsView.as_view(), name='teacher_update'),     # Обновление групп в которых преподает препод
    path('add_subjects/<int:pk>', TeacherSubjectsView.as_view(), name='add_subjects'),  # Добавление дисциплин преподавателя
    path('my_groups', TeacherGroupsView.as_view(), name='my_groups'),   # Получение групп в которых преподает препод

    path('add_user', CreateUser.as_view(), name='add_user'),    # Добавление пользователя
]
