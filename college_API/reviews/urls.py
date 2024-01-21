from django.urls import path
from .views import ReviewCreate, GetReview


urlpatterns = [
    path('get_comments', GetReview.as_view(), name='get_comments'),
    path('create_comment', ReviewCreate.as_view(), name='create_comment'),
    # path('delete_comment/<int:lecture_id>', DeleteCommentView.as_view(), name='delete_comment'),
]

# /<int:lecture_id>
