from django.urls import path

from .views import CreateExamView, UpdateExamView, DestroyExamView, TeacherExamsView, StudentExamsView, PassExamView, \
    StudentResultsView, TeacherResultsView


urlpatterns = [
    path('passing_exam/<int:exam_id>', PassExamView.as_view(), name='passing_exam'),

    path('create_exam', CreateExamView.as_view(), name='create_exam'),
    path('update_exam/<int:pk>', UpdateExamView.as_view(), name='update_exam'),
    path('delete_exam/<int:pk>', DestroyExamView.as_view(), name='delete_exam'),

    path('my_exams/', TeacherExamsView.as_view(), name='my_exams'),
    path('my_exams_student/', StudentExamsView.as_view(), name='my_exams_student'),

    path('student_results/', StudentResultsView.as_view(), name='student_results'),
    path('teacher_exams_results/', TeacherResultsView.as_view(), name='teacher_exams_results'),
]
