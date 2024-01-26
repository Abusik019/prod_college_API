from django.urls import path

from .views import CreateExamView, UpdateExamView, DestroyExamView, TeacherExamsView


urlpatterns = [
    path('create_exam', CreateExamView.as_view(), name='create_exam'),
    path('update_exam/<int:pk>', UpdateExamView.as_view(), name='update_exam'),
    path('delete_exam/<int:pk>', DestroyExamView.as_view(), name='delete_exam'),
    path('my_exams/', TeacherExamsView.as_view(), name='my_exams'),
]
