from comic.models import Project, Volume, Scene
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "image"]


class VolumeForm(ModelForm):
    class Meta:
        model = Volume
        fields = ["project", "name", "order"]


class SceneForm(ModelForm):
    class Meta:
        model = Scene
        fields = [ "number", "volume"]
