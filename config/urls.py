
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api.views import GenerateShortUrl, GetFullUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', GenerateShortUrl.as_view()),
    path('<str:short_url>', GetFullUrl.as_view()),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)