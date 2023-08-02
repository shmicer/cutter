import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class CustomURLValidator:
    def __call__(self, value):
        # Regular expression to validate URLs without the protocol
        url_regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )

        if not url_regex.match(value):
            raise ValidationError(_('Enter a valid URL without the protocol.'))
