from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializers import URLSerializer
from urllib.parse import urlsplit, urlunsplit

# Create your views here.
class URLShortenerAPIView(APIView):
    def post(self, request, *args, **kwargs):
        origin_link = request.data.get('url')
        if not origin_link:
            return Response({"error": "url is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # DB에 저장된 URL 확인
        url, created = URL.objects.get_or_create(origin_link=origin_link)
        
        if not created:
            short_url = self.create_short_url(origin_link, url.num)
            return Response({"url": short_url}, status=status.HTTP_200_OK)
        
        # DB에 저장된 URL의 short_url 생성
        short_url = self.create_short_url(origin_link, url.num)
        
        return Response({"url": short_url}, status=status.HTTP_201_CREATED)
    
    def create_short_url(self, origin_link, num):
        split_url = urlsplit(origin_link)
        path_parts = split_url.path.rstrip('/').split('/')
        path_parts[-1] = str(num)
        new_path = '/'.join(path_parts)
        short_url = urlunsplit((split_url.scheme, split_url.netloc, new_path, split_url.query, split_url.fragment))
        return short_url