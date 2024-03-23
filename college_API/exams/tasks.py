from celery import shared_task
from django.utils import timezone
from .models import Exam


@shared_task
def delete_expired_exams():
    """
    Задача для удаления истекших экзаменов.
    """
    current_time = timezone.now()
    exams_to_delete = Exam.objects.filter(end_time__lt=current_time)

    for exam in exams_to_delete:
        exam.delete()
