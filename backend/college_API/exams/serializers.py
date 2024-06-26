from random import shuffle

from rest_framework import serializers

from .models import Answer, Question, Exam, ExamResult


class AnswerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Answer.
    """
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Question.
    """
    # Сериализатор вложенной модели Answer, который будет использоваться для вложенного представления ответов
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']


# ___________________________________________________________________________________________________


class ExamSerializer(serializers.ModelSerializer):
    """
    Сериализатор экзамена.
    """
    questions = QuestionSerializer(many=True)   # Вложенный сериализатор для вопросов

    class Meta:
        model = Exam
        fields = ['id', 'title', 'groups', 'quantity_questions', 'time', 'ended', 'start_time', 'end_time', 'questions']

    def to_representation(self, instance):
        """
        Переопределение метода to_representation для фильтрации полей.
        """
        if self.context.get('view') and self.context['view'].__class__.__name__ != 'GetMyExam':
            data = super().to_representation(instance)
            # Удаление поля is_correct из данных о вопросах
            data['questions'] = self.remove_is_correct(data['questions'])
            return data
        else:
            return super().to_representation(instance)

    def remove_is_correct(self, data):
        """
        Удаление поля is_correct из данных.
        """
        if isinstance(data, dict):
            return {key: self.remove_is_correct(value) for key, value in data.items() if key != 'is_correct'}
        elif isinstance(data, list):
            return [self.remove_is_correct(item) for item in data]
        return data

    def get_questions(self, obj):
        """
        Метод для определения вопросов экзамена в случайном порядке и ограничения их количества
        """
        questions = list(obj.questions.all())  # Получаем все вопросы экзамена в виде списка
        shuffle(questions)  # Перемешиваем вопросы
        quantity = obj.quantity_questions  # Получаем количество вопросов, которое необходимо вывести
        # Возвращаем только указанное количество вопросов или все вопросы, если их количество меньше указанного
        return QuestionSerializer(questions[:quantity], many=True).data

    def create(self, validated_data):
        """
        Переопределение метода create для создания экзамена с вопросами и ответами.
        """
        # Извлечение данных о вопросах и группах из validated_data
        questions_data = validated_data.pop('questions', [])
        groups_data = validated_data.pop('groups', [])

        # Получение пользователя, отправившего запрос
        user = self.context['request'].user

        # Если пользователь - учитель, устанавливаем его как автора экзамена
        if hasattr(user, 'teacher_profile'):
            validated_data['author'] = user.teacher_profile

        # Создание объекта экзамена с извлеченными данными
        exam = Exam.objects.create(**validated_data)

        # Установка связей между экзаменом и группами
        exam.groups.set(groups_data)

        # Создание вопросов и ответов для каждого вопроса
        for question_data in questions_data:
            # Извлечение данных о ответах из вопроса
            answers_data = question_data.pop('answers', [])
            # Создание объекта вопроса, связанного с экзаменом
            question = Question.objects.create(exam=exam, **question_data)

            # Создание ответов для каждого вопроса
            for answer_data in answers_data:
                # Создание объекта ответа и связывание его с вопросом
                Answer.objects.create(question=question, **answer_data)

        # Возвращаем созданный экзамен
        return exam

    def update(self, instance, validated_data):
        """
        Переопределение метода update для обновления данных экзамена.
        """
        # Обновление полей экзамена из validated_data
        instance.title = validated_data.get('title', instance.title)
        instance.groups.set(validated_data.get('groups', instance.groups))
        instance.quantity_questions = validated_data.get('quantity_questions', instance.quantity_questions)
        instance.time = validated_data.get('time', instance.time)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)

        # Извлечение данных о вопросах из validated_data
        questions_data = validated_data.get('questions', [])

        # Удаление всех текущих вопросов экзамена
        instance.questions.all().delete()

        # Создание новых вопросов и ответов для экзамена
        for question_data in questions_data:
            # Извлечение данных об ответах из вопроса
            answers_data = question_data.pop('answers', [])
            # Создание объекта вопроса и связывание его с экзаменом
            question = Question.objects.create(exam=instance, **question_data)

            # Создание объектов ответов и связывание их с вопросом
            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)

        # Сохранение обновленного экзамена
        instance.save()
        return instance


# ___________________________________________________________________________________________________


class StartExamSerializer(serializers.ModelSerializer):
    """
        Сериализатор начала экзамена.
        """
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = ['id', 'title', 'groups', 'quantity_questions', 'time', 'ended', 'start_time', 'end_time', 'questions']

    def get_questions(self, obj):
        """
        Метод для определения вопросов экзамена в случайном порядке и ограничения их количества
        """
        questions = list(obj.questions.all())  # Получаем все вопросы экзамена в виде списка
        shuffle(questions)  # Перемешиваем вопросы
        quantity = obj.quantity_questions  # Получаем количество вопросов, которое необходимо вывести
        # Возвращаем только указанное количество вопросов или все вопросы, если их количество меньше указанного
        return QuestionSerializer(questions[:quantity], many=True).data


# ___________________________________________________________________________________________________


class ExamListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вывода списка экзаменов
    """
    class Meta:
        model = Exam
        fields = ['id', 'title', 'author', 'groups', 'time', 'start_time', 'end_time', 'ended']


class ExamResultSerializer(serializers.ModelSerializer):
    """
    Сериализатор результата экзамена
    """
    class Meta:
        model = ExamResult
        fields = ['exam', 'student', 'score']
