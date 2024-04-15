from django.urls import path
from .views import group_list, GroupMembersView, subjects_list, CreateLectureView, TeacherLecturesView, MyLecturesView, \
    LectureDetailView, DeleteLectureView, UpdateLectureView

urlpatterns = [
    # Эндпоинты для групп
    path('get_groups', group_list, name='group_list'),  # Все группы
    path('group_members/<int:pk>/', GroupMembersView.as_view(), name='group_members'),  # Члены группы
    path('get_subjects/', subjects_list, name='subjects_list'),   # Все дисциплины

    # Эндпоинты для лекций
    path('create_lecture/', CreateLectureView.as_view(), name='create_lecture'),    # Создание лекции
    path('delete_lecture/<int:pk>/', DeleteLectureView.as_view(), name='delete_lecture'),   # Удаление лекции
    path('lecture_detail/<int:lecture_id>/', LectureDetailView.as_view(), name='lecture_detail'),   # Просмотр лекции
    path('get_lectures/<int:teacher_id>/', TeacherLecturesView.as_view(), name='get_lectures'),     # Просмотр лекций препода
    path('my_lectures/', MyLecturesView.as_view(), name='my_lectures'),     # Просмотр собственных лекций
    path('update_lecture/<int:pk>/', UpdateLectureView.as_view(), name='update_lecture'),   # Изменение лекции
]
