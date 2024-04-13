from django.urls import path

from .views import (
    PassExamView,
    CreateExamView,
    UpdateExamView,
    DestroyExamView,
    TeacherExamsView,
    StudentExamsView,
    StudentResultsView,
    TeacherResultsView,
    GetListTeacherExams,
    GetMyExam,
    StartExam,
)


urlpatterns = [
    # Путь для прохождения экзамена
    path('passing_exam/<int:pk>', PassExamView.as_view(), name='passing_exam'),
    # Путь для начала экзамена
    path('start_exam/<int:pk>', StartExam.as_view(), name='start_exam'),
    # Путь для просмотра экзаменов препода
    path('get_list_teacher_exams/<int:pk>', GetListTeacherExams.as_view(), name='get_list_teacher_exams'),

    # Пути для создания, обновления и удаления экзамена
    path('create_exam', CreateExamView.as_view(), name='create_exam'),
    path('update_exam/<int:pk>', UpdateExamView.as_view(), name='update_exam'),
    path('delete_exam/<int:pk>', DestroyExamView.as_view(), name='delete_exam'),

    # Пути для просмотра списка экзаменов учителя и студента
    path('my_exams/', TeacherExamsView.as_view(), name='my_exams'),
    path('my_exams_student/', StudentExamsView.as_view(), name='my_exams_student'),
    # Путь для просмотра учителем его экзамена
    path('get_my_exam/<int:pk>', GetMyExam.as_view(), name='get_my_exam'),

    # Пути для просмотра результатов экзаменов студента и учителя
    path('student_results/', StudentResultsView.as_view(), name='student_results'),
    path('teacher_exams_results/', TeacherResultsView.as_view(), name='teacher_exams_results'),
]
