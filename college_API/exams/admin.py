from django.contrib import admin
from .models import Exam, Question, Answer


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
