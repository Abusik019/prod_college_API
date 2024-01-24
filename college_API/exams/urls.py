from django.urls import path

from .views import CreateExamView


urlpatterns = [
    path('create_exam', CreateExamView.as_view(), name='create_exam')
]
