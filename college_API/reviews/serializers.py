from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        write_only=True,
    )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = f'{instance.author.last_name} {instance.author.first_name}' if instance.author else None
        data['author_id'] = instance.author.id if instance.author else None
        return data

    def get_comments_for_lecture(self, lecture_id):
        comments = Review.objects.filter(lecture_id=lecture_id)
        return self.to_representation(comments, many=True)

    class Meta:
        model = Review
        fields = ['id', 'author', 'lecture', 'parent', 'text', 'created_at']
