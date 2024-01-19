from django.urls import path
from .views import group_list, GroupMembersView, subjects_list, CreateLectureView, TeacherLecturesView, MyLecturesView, \
    LectureDetailView, DeleteLectureView, UpdateLectureView

urlpatterns = [
    path('get_groups', group_list, name='group_list'),
    path('group_members/<int:group_id>/', GroupMembersView.as_view(), name='group_members'),
    path('get_subjects/', subjects_list, name='subjects_list'),

    path('create_lecture/', CreateLectureView.as_view(), name='create_lecture'),
    path('delete_lecture/<int:pk>/', DeleteLectureView.as_view(), name='delete_lecture'),
    path('lecture_detail/<int:lecture_id>/', LectureDetailView.as_view(), name='lecture_detail'),
    path('get_lectures/<int:teacher_id>/', TeacherLecturesView.as_view(), name='get_lectures'),
    path('my_lectures/', MyLecturesView.as_view(), name='my_lectures'),
    path('update_lecture/<int:pk>/', UpdateLectureView.as_view(), name='update_lecture'),
]
