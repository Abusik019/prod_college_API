import pytz
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from users.models import Student


def send_exam_notification(instance, created, **kwargs):
    if created:
        subject = 'Новый экзамен создан'
        message = f'Экзамен "{instance.title}" был создан. Начало: {instance.start_time}, Конец: {instance.end_time}'
        from_email = EMAIL_HOST_USER

        students = Student.objects.filter(group__exams=instance)
        recipient_list = [student.student.email for student in students]

        moscow_tz = pytz.timezone('Europe/Moscow')
        start_time_moscow = instance.start_time.astimezone(moscow_tz)
        end_time_moscow = instance.end_time.astimezone(moscow_tz)

        html_message = render_to_string('exam_created_email.html', {
            'author_name': instance.author.teacher.first_name,
            'author_surname': instance.author.teacher.last_name,
            'exam_title': instance.title,
            'exam_time': instance.time,
            'exam_start_time': start_time_moscow.strftime('%B-%d | %H:%M |'),
            'exam_end_time': end_time_moscow.strftime('%B-%d | %H:%M |'),
        })

        send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)


def send_result_notification(instance, created, **kwargs):
    if created:
        student = instance.student
        student_name = student.student.first_name
        student_surname = student.student.last_name

        subject = 'Студент прошел экзамен'
        message = f'Студент {student_name} {student_surname} прошел экзамен "{instance.exam.title}"'

        from_email = EMAIL_HOST_USER
        teacher = instance.exam.author
        recipient_list = [teacher.teacher.email]

        html_message = render_to_string('exam_result_email.html', {
            'teacher_name': teacher.teacher.first_name,
            'teacher_surname': teacher.teacher.last_name,
            'student_name': student_name,
            'student_surname': student_surname,
            'exam_result_score': instance.score,
            'exam_title': instance.exam.title,
        })

        send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
