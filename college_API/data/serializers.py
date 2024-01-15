from rest_framework import serializers
from .models import Group, Subject


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