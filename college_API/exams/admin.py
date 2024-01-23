from django.contrib import admin
from .models import Exam, Question, Answer
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]


class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'start_time', 'end_time')
    filter_horizontal = ('groups',)
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'exam')
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)


schedule, created = IntervalSchedule.objects.get_or_create(every=60, period=IntervalSchedule.SECONDS)
existing_task = PeriodicTask.objects.filter(name='DeleteExams').first()

if existing_task:
    existing_task.interval = schedule
    existing_task.task = 'exams.tasks.delete_expired_exams'
    existing_task.save()
else:
    exams = PeriodicTask.objects.create(
        interval=schedule,
        name='DeleteExams',
        task='tasks.delete_expired_exams'
    )
