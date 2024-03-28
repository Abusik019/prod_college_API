from django.contrib import admin
from .models import Exam, Question, Answer, ExamResult
from django_celery_beat.models import PeriodicTask, IntervalSchedule


# Определение класса Inline-модели для ответов
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


# Определение класса Inline-модели для вопросов
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]  # Добавление встроенной модели ответов


# Регистрация модели экзамена в админке
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'start_time', 'end_time')  # Отображаемые поля в списке экзаменов
    filter_horizontal = ('groups',)  # Используем фильтр с множественным выбором групп
    inlines = [QuestionInline]  # Добавляем встроенную модель вопросов


# Регистрация модели вопроса в админке
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'exam')  # Отображаемые поля в списке вопросов
    inlines = [AnswerInline]  # Добавляем встроенную модель ответов


# Регистрация модели ответа в админке
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')  # Отображаемые поля в списке ответов


# Регистрация модели результата экзамена в админке
@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('exam', 'student', 'score')  # Отображаемые поля в списке результатов экзаменов


# ________________________________________________________________________________________________________________


# Получаем или создаем интервальное расписание выполнения задачи
schedule, created = IntervalSchedule.objects.get_or_create(every=60, period=IntervalSchedule.SECONDS)

# Проверяем, существует ли уже периодическая задача с именем 'EndedExams'
existing_task = PeriodicTask.objects.filter(name='EndedExams').first()

# Если задача уже существует, обновляем ее параметры
if existing_task:
    existing_task.interval = schedule  # Обновляем интервал выполнения задачи
    existing_task.task = 'exams.tasks.end_expired_exams'  # Обновляем функцию-обработчик задачи
    existing_task.save()  # Сохраняем обновленную задачу
else:
    # Если задачи еще нет, создаем новую
    exams = PeriodicTask.objects.create(
        interval=schedule,  # Устанавливаем интервал выполнения задачи
        name='EndedExams',  # Устанавливаем имя задачи
        task='tasks.end_expired_exams'  # Устанавливаем функцию-обработчик задачи
    )
