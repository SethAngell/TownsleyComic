from comic.views import HomeView, ComicView

from django.urls import path

static_url_patterns = [path("", HomeView), path("comic/", ComicView)]
