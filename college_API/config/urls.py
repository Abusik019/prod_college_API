from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView

from .yasg import urlpatterns as doc_urls
from users.views import CustomStudentTokenObtainPairView, CustomTeacherTokenObtainPairView



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/users/', include('users.urls')),
    # path('api/v1/news/', include('news.urls')),
    # path('api/v1/lectures/', include('lectures.urls')),

    path('api/token/student/', CustomStudentTokenObtainPairView.as_view(), name='student_token_obtain_pair'),
    path('api/token/teacher/', CustomTeacherTokenObtainPairView.as_view(), name='teacher_token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += doc_urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
