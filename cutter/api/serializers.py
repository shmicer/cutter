from rest_framework import serializers
from rest_framework import status
from .services import generate_short_url
from .models import Url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ('url', 'short_url')
        extra_kwargs = {'url': {'validators': []}}

    def save(self):
        if self.instance is None:
            url_obj, created = Url.objects.get_or_create(url=self.validated_data['url'])
            if created:
                status_code = status.HTTP_201_CREATED
            else:
                status_code = status.HTTP_200_OK
            if not url_obj.short_url:
                url_obj.short_url = generate_short_url()
                url_obj.save()
            return url_obj, status_code

















