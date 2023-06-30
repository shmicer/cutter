from urllib import request

from django.db import models
from django.contrib.sites.models import Site


'''
1. Приложение должно получать ссылку через POST запрос
2. Должно обрабтотать и сгенерить короткую ссылку после доменного имени
3. При переходе по короткой ссылке должна отработать функция редиректа на оригинальную ссылку через приложение
4. Нужно подключить телеграм бота, при запросе к которому он также выдает короткую ссылку
5. Можно добавить генерабор qr-кодов для перехода по ссылке при наведении камеры
'''
current_site = Site.objects.get_current(request)


class Url(models.Model):
    url = models.URLField(unique=True, max_length=400)
    short_url = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @property
    def full_url(self):
        return f"{current_site.domain}/{self.short_url}"






