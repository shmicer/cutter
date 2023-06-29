from django.contrib import admin

from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'short_url',
        'created',
        'is_active'
    )
    search_fields = ('url', 'short_url')
    ordering = ('-created',)
