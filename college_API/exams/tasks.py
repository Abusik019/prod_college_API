from celery import shared_task
from django.utils import timezone
from .models import Exam


@shared_task
def delete_expired_exams():
    current_time = timezone.now()
    exams_to_delete = Exam.objects.filter(end_time__lt=current_time)

    for exam in exams_to_delete:
        exam.delete()
