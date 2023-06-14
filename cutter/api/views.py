from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UrlSerializer
from .services import generate_short_url


class ShortUrlAPIView(APIView):

    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(short_url=generate_short_url())
        return Response(serializer.data)











