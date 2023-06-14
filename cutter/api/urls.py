from django.urls import path

from .views import ShortUrlAPIView

app_name = 'api'

urlpatterns = [
    path('url/', ShortUrlAPIView.as_view()),
]