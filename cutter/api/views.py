from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect


from .models import Url
from .serializers import UrlSerializer
# from .services import get_full_url


class GenerateShortUrl(APIView):

    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url, status_code = serializer.save()
        # if created:
        #     status_code = status.HTTP_201_CREATED
        # else:
        #     status_code = status.HTTP_200_OK
        return Response(UrlSerializer(url).data, status_code)


class GetFullUrl(APIView):

    def get(self, request, short_url):
        url_object = get_object_or_404(Url, short_url=short_url)
        full_link = url_object.url
        return redirect(full_link)











