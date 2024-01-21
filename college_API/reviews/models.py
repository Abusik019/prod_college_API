from django.db import models
from django.utils import timezone

from users.models import User
from data.models import Lecture


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='review')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='parent', blank=True, null=True)

    text = models.TextField('Сообщение', max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author} - {self.lecture}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
