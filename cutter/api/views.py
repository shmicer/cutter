from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import redirect

from .models import Url
from .serializers import UrlSerializer
from .services import get_full_url, generate_short_url


class GenerateShortUrl(APIView):

    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url, status_code = serializer.create(
            validated_data=serializer.validated_data
            )
        return Response(UrlSerializer(url).data, status=status_code)


class GetFullUrl(APIView):

    def get(self, request, short_url):

        full_link = get_full_url(short_url)
        return redirect(full_link)











