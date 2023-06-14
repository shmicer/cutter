from rest_framework import serializers

from .models import Url
from .services import generate_short_url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = '__all__'









