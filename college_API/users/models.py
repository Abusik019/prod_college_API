from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from data.models import Group, Subject


class User(AbstractUser):
    password = models.CharField(max_length=128, null=True, blank=True)
    college_id = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150, default='-')
    last_name = models.CharField(max_length=150, default='-')
    email = email = models.EmailField(blank=True, null=True, default='')
    username = models.CharField(unique=True, max_length=150, null=True, blank=True)
    image = models.CharField(null=True, blank=True)

    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' or self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='student_profile', null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name='student_group', blank=True, null=True)

    def __str__(self):
        return f'{self.student}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='teacher_profile', null=True)
    subjects = models.ManyToManyField(Subject, related_name='teacher_subject', blank=True)
    group = models.ManyToManyField(Group, related_name='teacher_groups', blank=True)

    def __str__(self):
        return f'{self.teacher}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


# ____________________________________________________________________________________________________


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


