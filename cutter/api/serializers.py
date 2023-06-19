from rest_framework import serializers

from .services import generate_short_url
from .models import Url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ('url', 'short_url')
        # extra_kwargs = {'url': {'validators': []}}

    def save(self):
        if self.instance is None:
            encoded_url = generate_short_url()
            return Url.objects.get_or_create(url=self.validated_data['url'], short_url=encoded_url)









