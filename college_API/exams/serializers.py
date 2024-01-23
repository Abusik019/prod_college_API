from rest_framework import serializers

from .models import Exam, Question, Answer
from users.models import Teacher
from data.models import Group


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'answers')


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    class Meta:
        model = Exam
        fields = ('id', 'title', 'groups', 'time', 'start_time', 'end_time', 'questions')

    def create(self, validated_data):
        author = self.context['request'].user.teacher_profile
        validated_data['author'] = author
        questions_data = validated_data.pop('questions', [])
        groups_data = validated_data.pop('groups', [])
        exam = Exam.objects.create(**validated_data)

        exam.groups.set(groups_data)

        for question_data in questions_data:
            answers_data = question_data.pop('answers', [])
            question = Question.objects.create(exam=exam, **question_data)

            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)

        return exam
