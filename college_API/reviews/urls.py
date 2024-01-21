from django.urls import path
from .views import ReviewCreate, GetReviewForLecture, DeleteReview

urlpatterns = [
    path('get_comments/<int:lecture_id>/', GetReviewForLecture.as_view(), name='get_comments'),
    path('create_comment', ReviewCreate.as_view(), name='create_comment'),
    path('delete_comment/<int:pk>', DeleteReview.as_view(), name='delete_comment'),
]
