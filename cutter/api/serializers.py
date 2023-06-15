from rest_framework import serializers, status

from .services import get_full_url, generate_short_url
from .models import Url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = '__all__'
        extra_kwargs = {'url': {'validators': []}}

    def create(self, validated_data):
        full_url = validated_data['url']
        short_url = generate_short_url()
        url_object, created = Url.objects.get_or_create(url=full_url, short_url=short_url)
        if created:
            status_code = status.HTTP_201_CREATED
        else:
            status_code = status.HTTP_200_OK
        return url_object, status_code









