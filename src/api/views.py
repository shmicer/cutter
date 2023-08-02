import base64

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

from .models import Url
from .serializers import UrlSerializer
from .services import generate_qr


class GenerateShortUrl(APIView):

    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url, created = serializer.save()
        if created:
            status_code = status.HTTP_201_CREATED
        else:
            status_code = status.HTTP_200_OK
        short_link = url.full_url
        qr_code = generate_qr(short_link)
        qr_code_base64 = base64.b64encode(qr_code).decode('utf-8')
        return Response({
            'short_link': short_link,
            'qr_code': qr_code_base64
        }, status=status_code)


class GetFullUrl(APIView):

    def get(self, request, short_url):
        url_object = get_object_or_404(Url, short_url=short_url)
        if url_object.url.startswith(('http://', 'https://')):
            full_link = url_object.url
        elif url_object.url.startswith('www.'):
            full_link = f'https://{url_object.url[4:]}'
        else:
            full_link = f'https://{url_object.url}'
        url_object.redirect_count += 1
        url_object.save()
        return redirect(full_link)
