from django.contrib import admin
from .models import Facult, Course, PodGroup, Group, Subject, Lecture


@admin.register(Facult)
class FacultAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PodGroup)
class PodGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('facult', 'course', 'podgroup')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer')

