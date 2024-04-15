import pytz
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string


def lecture_create_notification(instance, created, **kwargs):
    """
    Отправляет сообщение студенту, если преподаватель,
    ведущий у него в группе создает новую лекцию.
    """
    if created:
        lecturer = instance.lecturer                    # Преподаватель создавший лекцию
        lecturer_name = lecturer.teacher.first_name     # Извлечение имени и фамилии препода
        lecturer_surname = lecturer.teacher.last_name
        lecture = instance.title                        # Название материала

        subject = 'У вас новая лекция!'
        message = f'{lecturer_name} {lecturer_surname} выложил(а) новую лекцию.'    # Сообщение
        from_email = EMAIL_HOST_USER                                                # email колледжа

        recipient = [student.student.email for group in instance.group.all() for student in group.student_group.all()]
        """
        Цикл перебирающий сначала все группы к которым привязана лекция,
        затем всех студентов этой группы, добавляя их email в массив.
        """

        moscow_tz = pytz.timezone('Europe/Moscow')
        time_moscow = instance.created_at.astimezone(moscow_tz)

        html_message = render_to_string('created_lecture_email.html', {
            'lecture': lecture,
            'lecturer_name': lecturer_name,
            'lecturer_surname': lecturer_surname,
            'created_at': time_moscow.strftime('%B-%d | %H:%M |'),
        })

        send_mail(subject, message, from_email, recipient, fail_silently=False, html_message=html_message)
