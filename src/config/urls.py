from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from api.views import GenerateShortUrl, GetFullUrl


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('efjn32fjkerjgfk34g/admin', admin.site.urls),
    path('url', GenerateShortUrl.as_view()),
    path('<str:short_url>', GetFullUrl.as_view()),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)