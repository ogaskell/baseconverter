"""URL definitions for the baseconverter app."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('convert', views.convert, name="convert"),
    path('supported', views.supported, name="supported")
]
