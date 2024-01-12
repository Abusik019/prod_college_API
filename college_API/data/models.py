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
