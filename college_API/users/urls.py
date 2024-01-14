from django.urls import path
from .views import user_list, student_list, teacher_list




urlpatterns = [
    path('get_users', user_list, name='get_users'),
    path('get_students', student_list, name='get_students'),
    path('get_teacher', teacher_list, name='get_teacher'),
    # path('update_teacher_profile', update_teacher_profile, name='update_teacher_profile'),
]

