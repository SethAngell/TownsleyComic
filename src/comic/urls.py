from comic.views import (
    ComicView,
    ProjectIndexView,
    ProjectDetailView,
    ProjectEditView,
    ProjectCreateView,
    VolumeIndexView,
    VolumeDetailView,
    VolumeEditView,
    VolumeCreateView,
    SceneDetailView,
    SceneEditView,
)

from django.urls import path

static_url_patterns = [
    path("", ComicView),
    path("project/index/", ProjectIndexView),
    path("project/create/", ProjectCreateView),
    path("project/<int:id>/", ProjectDetailView),
    path("project/edit/<int:id>/", ProjectEditView),
    path("volume/index/", VolumeIndexView),
    path("volume/create/", VolumeCreateView),
    path("volume/<int:id>/", VolumeDetailView),
    path("volume/edit/<int:id>/", VolumeEditView),
    path("scene/<int:id>/", SceneDetailView),
    path("scene/edit/<int:id>/", SceneEditView),
]
