from django.contrib.auth.models import AbstractUser, Permission
from django.db import models



class Facult(models.Model):
    name = models.CharField('Факультет', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Course(models.Model):
    name = models.CharField('Курс', max_length=5)

    def __str__(self):
        return f"{self.name} курс"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Group(models.Model):
    name = models.CharField('Группа', max_length=5)

    def __str__(self):
        return f"{self.name} группа"

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


# __________________________________________________________________________________________



class Student(AbstractUser):
    student_id = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150, null=True, blank=False)
    last_name = models.CharField(max_length=150, null=True, blank=False)
    image = models.CharField(null=True, blank=True)

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, default='')
    facult = models.ForeignKey(Facult, on_delete=models.SET_NULL, null=True, blank=True, default='')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, default='')

    groups = models.ManyToManyField(Group, related_name='students')
    user_permissions = models.ManyToManyField(Permission, related_name='student_users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}' or self.username

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teacher(AbstractUser):
    first_name = models.CharField('Имя', max_length=150, null=True, blank=False)
    surname = models.CharField('Фамилия', max_length=150, null=True, blank=False)
    last_name = models.CharField('Отчество', max_length=150, null=True, blank=False)

    facult = models.ManyToManyField(Facult, related_name='teachers', blank=True)
    groups = models.ManyToManyField(Group, related_name='teachers', blank=True)
    courses = models.ManyToManyField(Course, related_name='teachers', blank=True)

    user_permissions = models.ManyToManyField(Permission, related_name='teacher_users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}' or self.username

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
