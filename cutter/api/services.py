from django.http import HttpResponse
from django.conf import settings
import random
from .models import Url


def generate_short_url():
    short_url = ''.join(random.choices(settings.CHARACTERS, k=settings.URL_LENGTH))
    return short_url

def get_full_url(url):
    try:
        url_object = Url.objects.get(short_url=url)
        if not url_object.is_active:
            raise KeyError('URL is no longer available')
    except Url.DoesNotExist:
        raise KeyError('Try another url. No such urls in DB')
    return url_object.original_url







