import pytz
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string


def send_review_notification(instance, created, **kwargs):
    """
    Функция отправки уведомления о новом комментарии под лекцией препода.
    """
    if created:
        # Извлечение данных из запроса
        author = instance.author
        author_name = author.first_name
        author_surname = author.last_name
        lecture = instance.lecture.title

        # Сообщение
        subject = 'У вас новый комментарий!'
        message = f'Комментарий от {author_name} {author_surname} был опубликован под лекцией "{lecture}"'
        # Почта отправителя
        from_email = EMAIL_HOST_USER

        # Извлечение почты препода
        recipient = [instance.lecture.lecturer.teacher.email]

        moscow_tz = pytz.timezone('Europe/Moscow')
        time_moscow = instance.created_at.astimezone(moscow_tz)

        # Формирование html сообщения
        html_message = render_to_string('review_created_email.html', {
            'lecture': lecture,
            'author_name': author_name,
            'author_surname': author_surname,
            'text': instance.text,
            'created_at': time_moscow.strftime('%B-%d | %H:%M |'),
        })

        # Отправка сообщения
        send_mail(subject, message, from_email, recipient, fail_silently=False, html_message=html_message)


def send_reply_notification(instance, created, **kwargs):
    """
    Функция отправки уведомления об ответе на коментарий.
    """
    if created:
        # Извлечение данных из запроса
        author = instance.author
        author_name = author.first_name
        author_surname = author.last_name
        lecture = instance.lecture.title

        # Сообщение
        subject = 'Вам ответили на комментарий!'
        message = f'{author_name} {author_surname} ответил на ваш комментарий под лекцией "{lecture}"'
        # Почта отправителя
        from_email = EMAIL_HOST_USER

        # Извлечение почты автора коментария на который ответили
        recipient = [instance.parent.author.email]

        moscow_tz = pytz.timezone('Europe/Moscow')
        time_moscow = instance.created_at.astimezone(moscow_tz)

        # Формирование html сообщения
        html_message = render_to_string('reply_email.html', {
            'lecture': lecture,
            'author_name': author_name,
            'author_surname': author_surname,
            'text': instance.text,
            'created_at': time_moscow.strftime('%B-%d | %H:%M |'),
        })

        # Отправка сообщения
        send_mail(subject, message, from_email, recipient, fail_silently=False, html_message=html_message)
