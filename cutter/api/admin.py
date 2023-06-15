from django.contrib import admin

from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'short_url',
        'created_date',
        'is_active'
    )
    search_fields = ('original_url', 'short_url')
    ordering = ('-created_date',)
