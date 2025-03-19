from django.urls import path
from .views import shorten_url, redirect_url


urlpatterns = [
    path("api/shorten/", shorten_url, name="api-shorten"),
    path("<str:short_code>/", redirect_url, name="redirect")
]