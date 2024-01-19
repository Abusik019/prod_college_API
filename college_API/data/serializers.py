from rest_framework import serializers
from .models import Group, Subject, Lecture


class GroupSerializer(serializers.ModelSerializer):
    facult_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    podgroup_name = serializers.SerializerMethodField()

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

    class Meta:
        model = Subject
        fields = '__all__'


class CreateLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['title', 'image', 'description', 'file', 'group']

    def create(self, validated_data):
        teacher = self.context['request'].user.teacher_profile
        validated_data['lecturer'] = teacher

        groups_data = validated_data.pop('group', [])
        groups_list = list(groups_data)

        for group in groups_list:
            if group not in teacher.group.all():
                return 'Error'

        lecture = Lecture.objects.create(**validated_data)
        lecture.group.set(groups_data)

        return lecture
