from rest_framework import serializers

from .models import Answer, Question, Exam, ExamResult


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'groups', 'time', 'start_time', 'end_time', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        groups_data = validated_data.pop('groups', [])

        user = self.context['request'].user
        if hasattr(user, 'teacher_profile'):
            validated_data['author'] = user.teacher_profile

        exam = Exam.objects.create(**validated_data)
        exam.groups.set(groups_data)

        for question_data in questions_data:
            answers_data = question_data.pop('answers', [])
            question = Question.objects.create(exam=exam, **question_data)

            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)

        return exam

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.groups.set(validated_data.get('groups', instance.groups))
        instance.time = validated_data.get('time', instance.time)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)

        questions_data = validated_data.get('questions', [])

        instance.questions.all().delete()

        for question_data in questions_data:
            answers_data = question_data.pop('answers', [])
            question = Question.objects.create(exam=instance, **question_data)

            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)

        instance.save()
        return instance


class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ['exam', 'student', 'score']


# _______________________________________________________________________________________________________________


class AnswerOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']


class QuestionOnlySerializer(serializers.ModelSerializer):
    answers = AnswerOnlySerializer(many=True)

    class Meta:
        model = Question
        fields = ['text', 'answers']
