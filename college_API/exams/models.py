from django.db import models
from django.utils import timezone
from users.models import Teacher
from data.models import Group


class Exam(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название теста')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='exams', verbose_name='Автор')
    groups = models.ManyToManyField(Group, related_name='exams', verbose_name='Группы')
    time = models.IntegerField('Время на выполнение')
    start_time = models.DateTimeField(verbose_name='Дата и время начала', default=timezone.now)
    end_time = models.DateTimeField(verbose_name='Дата и время окончания', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions', verbose_name='Экзамен')
    text = models.TextField(verbose_name='Текст вопроса')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name='Вопрос')
    text = models.CharField(max_length=255, verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Верный ответ')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
