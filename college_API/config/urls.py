from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/users/', include('users.urls')),
    # path('api/v1/news/', include('news.urls')),
    # path('api/v1/lectures/', include('lectures.urls')),
]

urlpatterns += doc_urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
