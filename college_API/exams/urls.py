from django.urls import path

from .views import CreateExam


urlpatterns = [
    path('create_exam', CreateExam.as_view(), name='create_exam')
]
