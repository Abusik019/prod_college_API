from django.urls import path

from .views import CreateExamView, UpdateExamView, DestroyExamView


urlpatterns = [
    path('create_exam', CreateExamView.as_view(), name='create_exam'),
    path('update_exam/<int:pk>', UpdateExamView.as_view(), name='update_exam'),
    path('delete_exam/<int:pk>', DestroyExamView.as_view(), name='delete_exam'),
]
