from celery import shared_task
from django.utils import timezone
from .models import Exam


@shared_task
def end_expired_exams():
    """
    Задача для удаления истекших экзаменов.
    """
    current_time = timezone.now()
    ended_exams = Exam.objects.filter(end_time__lt=current_time)

    for exam in ended_exams:
        exam.ended = True
        exam.save()
        