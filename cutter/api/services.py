from django.http import HttpResponse
from django.conf import settings
import random
# from .models import Url


def generate_short_url():
    short_url = ''.join(random.choices(settings.CHARACTERS, k=settings.URL_LENGTH))
    return short_url








