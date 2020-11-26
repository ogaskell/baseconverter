"""Functions to render pages."""

from django.shortcuts import render


def index(request):
    """Index page on site."""
    return render(request, 'baseconverter/index.html', {})
