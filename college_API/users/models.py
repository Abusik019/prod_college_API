from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



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
class User(AbstractUser):
    password = models.CharField(max_length=128, null=True, blank=True)
    college_id = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(unique=True, max_length=150, null=True, blank=True)
    image = models.CharField(null=True, blank=True)

    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' or self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', default=1)

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, default='')
    facult = models.ForeignKey(Facult, on_delete=models.SET_NULL, null=True, blank=True, default='')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, default='')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile', default=1)

    facult = models.ManyToManyField(Facult, related_name='teachers', blank=True)
    groups = models.ManyToManyField(Group, related_name='teachers', blank=True)
    courses = models.ManyToManyField(Course, related_name='teachers', blank=True)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            Teacher.objects.create(teacher=instance)
        else:
            Student.objects.create(student=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_teacher:
        instance.teacher_profile.save()
    else:
        instance.student_profile.save()


