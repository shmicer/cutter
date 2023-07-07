
from django.db import models
from django.contrib.sites.models import Site
current_site = Site.objects.get_current()


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
        return f"{current_site}/{self.short_url}"






