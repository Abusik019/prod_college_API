from django.urls import path
from .views import DestroyNews, UpdateNews, CreateNews, RetrieveNews, news_list


urlpatterns = [
    path('get_news', news_list, name='news_list'),
    path('news_detail/<int:pk>', RetrieveNews.as_view(), name='news_detail'),
    path('news_update/<int:pk>', UpdateNews.as_view(), name='news_update'),
    path('delete_news/<int:pk>', DestroyNews.as_view(), name='delete_news'),
    path('create_news', CreateNews.as_view(), name='create_news'),
]
