
from django.contrib import admin
from django.urls import path

from api.views import GenerateShortUrl, GetFullUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', GenerateShortUrl.as_view()),
    path('<str:short_url>', GetFullUrl.as_view()),
]
