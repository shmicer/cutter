import hashlib
from io import BytesIO

import qrcode


def generate_short_url(url):
    short_url = hashlib.shake_128(str(url).encode("utf-8")).hexdigest(3)
    return short_url


def generate_qr(url):
    bio = BytesIO()
    qr_code = qrcode.make(url)
    qr_code.save(bio, format='PNG')
    bio.seek(0)
    return bio.getvalue()
