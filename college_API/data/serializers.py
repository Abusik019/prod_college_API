from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .models import Group, Subject, Lecture


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор группы (факультет, курс, подгруппа)
    """
    facult_name = serializers.SerializerMethodField('get_facult_name')
    course_name = serializers.SerializerMethodField('get_course_name')
    podgroup_name = serializers.SerializerMethodField('get_podgroup_name')

    class Meta:
        model = Group
        fields = ['id', 'facult_name', 'course_name', 'podgroup_name']

    def get_facult_name(self, obj):
        return obj.facult.name if obj.facult else None

    def get_course_name(self, obj):
        return obj.course.name if obj.course else None

    def get_podgroup_name(self, obj):
        return obj.podgroup.name if obj.podgroup else None


class SubjectsSelializers(serializers.ModelSerializer):
    """
    Сериализатор дисциплины.
    """
    class Meta:
        model = Subject
        fields = '__all__'


# ______________________________________________________________________________________________________________


class CreateLectureSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания лекции
    """
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'image', 'description', 'file', 'group']

    def create(self, validated_data):
        """
        Переопределение метода create.
        """
        teacher = self.context['request'].user.teacher_profile  # Извлечение учителя из запроса.
        validated_data['lecturer'] = teacher

        groups_data = validated_data.pop('group', [])           # Извлечение групп из запроса в массив.
        groups_list = list(groups_data)

        for group in groups_list:                   # Цикл перебирающий все группы из массива
            if group not in teacher.group.all():    # Проверка на то, ведет ли препод занятия в этой группе
                return Response

        lecture = Lecture.objects.create(**validated_data)
        lecture.group.set(groups_data)

        return lecture

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.file = validated_data.get('file', instance.file)

        groups_data = validated_data.get('group', [])
        instance.group.set(groups_data)

        user = self.context['request'].user
        if hasattr(user, 'teacher_profile'):
            instance.lecturer = user.teacher_profile

        instance.save()
        return instance


class LectureSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField('get_file')
    image = serializers.SerializerMethodField('get_image')
    description = serializers.SerializerMethodField('get_description')

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'image', 'description', 'file', 'lecturer', 'group', 'created_at']

    def get_image(self, obj):
        return obj.image if obj.image != '' else None

    def get_description(self, obj):
        return obj.description if obj.description != '' else None

    def get_file(self, obj):
        return obj.file if obj.file != '' else None
