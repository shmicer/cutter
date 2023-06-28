import hashlib
from io import BytesIO

import aiogram
import qrcode
from django.conf import settings


def generate_short_url(url):
    short_url = hashlib.shake_128(str(url).encode("utf-8")).hexdigest(3)
    # short_url = ''.join(random.choices(settings.CHARACTERS, k=settings.URL_LENGTH))
    return short_url


def generate_qr(url):
    bio = BytesIO()
    qrcode.make(url).save(bio, 'PNG')
    bio.seek(0)
    return aiogram.types.BufferedInputFile(bio.getvalue(), "qrcode.png")








