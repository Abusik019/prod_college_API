from django.db import models
from django.utils import timezone
from users.models import Teacher, Student
from data.models import Group


class Exam(models.Model):
    """
    Модель экзамена.
    """
    title = models.CharField(max_length=255, verbose_name='Название теста')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='exams', verbose_name='Автор')
    groups = models.ManyToManyField(Group, related_name='exams', verbose_name='Группы')
    quantity_questions = models.IntegerField('Количество вопросов')
    time = models.IntegerField('Время на выполнение')
    ended = models.BooleanField('Закончился', default=False)
    start_time = models.DateTimeField(verbose_name='Дата и время начала', default=timezone.now)
    end_time = models.DateTimeField(verbose_name='Дата и время окончания', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'


class Question(models.Model):
    """
    Модель вопроса.
    """
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions', verbose_name='Экзамен')
    text = models.TextField(verbose_name='Текст вопроса')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """
    Модель ответа.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name='Вопрос')
    text = models.CharField(max_length=255, verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Верный ответ')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class ExamResult(models.Model):
    """
    Модель результата экзамена.
    """
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_results')
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.exam}-{self.student}'

    class Meta:
        verbose_name = 'Результат экзамена'
        verbose_name_plural = 'Результаты экзаменов'
