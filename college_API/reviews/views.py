from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .email_senders import send_review_notification, send_reply_notification
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsCommentOwnerOrLectureOwnerOrAdmin


class ReviewCreate(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        review = serializer.save()
        lecture_author = review.lecture.lecturer
        if f'{review.author}' != f'{lecture_author}':
            send_review_notification(instance=review, created=True)
        if review.parent is not None:
            send_reply_notification(instance=review, created=True)


class GetReviewForLecture(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lecture_id = self.kwargs['lecture_id']
        return Review.objects.filter(lecture_id=lecture_id)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteReview(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsCommentOwnerOrLectureOwnerOrAdmin]
