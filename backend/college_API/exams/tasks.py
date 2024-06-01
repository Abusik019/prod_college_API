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
    """
    Задача для удаления истекших экзаменов.
    """
    current_time = timezone.now()
    ended_exams = Exam.objects.filter(end_time__lt=current_time)

    for exam in ended_exams:
        exam.ended = True
        exam.save()


@shared_task
def send_exam_results():
    """
    Задача для отправки результатов экзамена в виде Excel-таблицы по электронной почте учителю.
    """
    current_time = timezone.now()
    ended_exams = Exam.objects.filter(end_time__lt=current_time, ended=True)

    for exam in ended_exams:
        # Получаем результаты экзамена
        results = exam.results.all()

        # Создаем DataFrame из результатов
        data = {
            'Группа': [result.student.group for result in results],
            'Студент': f'{[result.student.student.first_name for result in results]} {[result.student.student.last_name for result in results]}',
            'Оценка': [result.score for result in results],
        }
        df = pd.DataFrame(data)

        # Создаем путь к файлу
        file_path = f'/tmp/{exam.title}_results.xlsx'

        # Сохраняем DataFrame в Excel файл
        df.to_excel(file_path, index=False)

        # Отправляем файл по электронной почте
        subject = f'Результаты экзамена {exam.title}'
        body = f'В приложении результаты экзамена {exam.title}.'
        email = EmailMessage(subject, body, to=[exam.author.teacher.email])
        email.attach_file(file_path)
        email.send()

        # Удаляем временный файл
        os.remove(file_path)
