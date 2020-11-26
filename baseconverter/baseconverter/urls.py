"""URL definitions for the baseconverter app."""

from django.urls import path
from . import views

urlpatters = [
    path('', views.index, name="index"),
]
