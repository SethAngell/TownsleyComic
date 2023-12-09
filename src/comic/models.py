from django.db import models
from content.models import ImageContent
from accounts.models import CustomUser


# Create your models here.
class Project(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, null=True, blank=True)
    image = models.ForeignKey(
        ImageContent, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Volume(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class Scene(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volume}: {self.name}  - Scene {self.number}"


class Page(models.Model):
    number = models.IntegerField()
    content = models.ForeignKey(ImageContent, on_delete=models.PROTECT)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.scene} - Page {self.number}"
