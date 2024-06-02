from celery import shared_task
from django.utils import timezone
import pandas as pd
from celery import shared_task
from django.core.mail import EmailMessage
from django.utils import timezone
from .models import Exam
import os

from .models import Exam


@shared_task
def end_expired_exams():
    current_time = timezone.now()
    ended_exams = Exam.objects.filter(end_time__lt=current_time)

    for exam in ended_exams:
        results = exam.results.all()
        data = {
            'Группа': [result.student.group for result in results],
            'Студент': [f'{result.student.student.first_name} {result.student.student.last_name}' for result in
                        results],
            'Оценка': [result.score for result in results],
        }
        df = pd.DataFrame(data)

        file_path = f'/tmp/{exam.title}_results.xlsx'
        df.to_excel(file_path, index=False)

        subject = f'Результаты экзамена {exam.title}'
        body = f'В приложении результаты экзамена {exam.title}.'
        email = EmailMessage(subject, body, to=[exam.author.teacher.email])
        email.attach_file(file_path)
        email.send()

        os.remove(file_path)
        exam.ended = True
        exam.save()

