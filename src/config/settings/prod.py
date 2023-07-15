import socket  # only if you haven't already imported this
from .base import *  # noqa

DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ["cl2u.ru", "90.156.225.6"]
