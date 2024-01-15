from datetime import timezone
from django.db import models

# from users.models import User


class Facult(models.Model):
    name = models.CharField('Факультет', max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Course(models.Model):
    name = models.CharField('Курс', max_length=5)

    def __str__(self):
        return f"{self.name} курс"

    def __repr__(self):
        return f"{self.name} курс"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class PodGroup(models.Model):
    name = models.CharField('Группа', max_length=5)

    def __str__(self):
        return f"{self.name} подгруппа"

    def __repr__(self):
        return f"{self.name} подгруппа"

    class Meta:
        verbose_name = 'Подгруппа'
        verbose_name_plural = 'Подгруппы'


class Subject(models.Model):
    name = models.CharField('Название предмета', max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Group(models.Model):
    facult = models.ForeignKey(Facult, on_delete=models.SET_NULL, null=True, blank=True, default='', related_name='groups_facult')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, default='', related_name='groups_course')
    podgroup = models.ForeignKey(PodGroup, on_delete=models.SET_NULL, null=True, blank=True, default='', related_name='groups_podgroup')

    def __str__(self):
        return f"{self.facult} {self.course}, {self.podgroup}"

    def __repr__(self):
        return f"{self.facult} {self.course}, {self.podgroup}"

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


# ____________________________________________________________________________________________________________


# class Lecture(models.Model):
#     title = models.CharField('Название', max_length=300)
#     description = models.TextField('Описание')
#     lecturer = models.ForeignKey(User, verbose_name='Лектор', related_name='lecturer', on_delete=models.SET_NULL)
#     group = models.ManyToManyField(Group, blank=True, default='')
#     created_at = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Лекция'
#         verbose_name_plural = 'Лекции'