from rest_framework import serializers
from .services import generate_short_url
from .models import Url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ('url', 'short_url', 'qr')
        extra_kwargs = {'url': {'validators': []}}

    def save(self):
        """
        Save method checks if the object with requested full_url in the database. If not,
        generates short_url for this object and return it
        """
        if self.instance is None:
            original_url = self.validated_data['url']
            encoded_url = generate_short_url(original_url)
            url_obj = Url.objects.get_or_create(url=original_url,
                                                defaults={'short_url': encoded_url}
                                                )
            return url_obj

















