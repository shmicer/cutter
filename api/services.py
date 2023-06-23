import hashlib


def generate_short_url(url):
    """
    This function generates
    :param url:
    :return:
    """
    short_url = hashlib.shake_128(str(url).encode("utf-8")).hexdigest(3)
    # short_url = ''.join(random.choices(settings.CHARACTERS, k=settings.URL_LENGTH))
    return short_url








