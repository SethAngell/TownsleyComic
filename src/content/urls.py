from content.views import (
    ImageIndexView,
    ImageDetailView,
    ImageEditView,
    ImageCreateView,
)

from django.urls import path

static_url_patterns = [
    path("image_index/", ImageIndexView),
    path("image_create/", ImageCreateView),
    path("image_detail/<int:id>/", ImageDetailView),
    path("image_edit/<int:id>/", ImageEditView),
]
