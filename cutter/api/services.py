from django.http import HttpResponse

from .models import Url
from django.conf import settings
import random


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
    url_object.save()
    return url_object.original_url


def redirect(request, short_url):
    try:
        full_link = get_full_url(short_url)
        return redirect(full_link)
    except Exception as e:
        return HttpResponse(e.args)






