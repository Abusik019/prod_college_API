from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField('Название', max_length=150)
    description = models.CharField('Описание')
    image = models.CharField('Изображение')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
