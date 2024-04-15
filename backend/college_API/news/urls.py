from django.urls import path

from .views import (
    DestroyNews,
    UpdateNews,
    CreateNews,
    RetrieveNews,
    news_list
)


urlpatterns = [
    path('get_news', news_list, name='news_list'),                              # Просмотр новостей
    path('news_detail/<int:pk>', RetrieveNews.as_view(), name='news_detail'),   # Просмотр отдельной новости
    path('news_update/<int:pk>', UpdateNews.as_view(), name='news_update'),     # Обновление новости
    path('delete_news/<int:pk>', DestroyNews.as_view(), name='delete_news'),    # Удалить новость
    path('create_news', CreateNews.as_view(), name='create_news'),              # Создать новость
]
