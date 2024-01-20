from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import DestroyAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from .serializers import NewsSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import News


class DestroyNews(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]


class UpdateNews(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]


class RetrieveNews(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]


class CreateNews(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def news_list(request):
    queryset = News.objects.all()
    serializer = NewsSerializer(queryset, many=True)
    return Response(serializer.data)
