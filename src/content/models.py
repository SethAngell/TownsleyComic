from django.db import models

from accounts.models import CustomUser


def image_upload_location(instance, filename):
    return f"content/{instance.user.id}/images/{filename}"


def document_upload_location(instance, filename):
    return f"content/{instance.user.id}/documents/{filename}"


class ImageContent(models.Model):
    name = models.CharField(max_length=128)
    alt_text = models.TextField(max_length=1024, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_location, null=False, blank=True)


class FileContent(models.Model):
    name = models.CharField(max_length=128)
    alt_text = models.TextField(max_length=1024)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to=document_upload_location, null=False, blank=True)


class TextContent(models.Model):
    name = models.CharField(max_length=128)
    source = models.ForeignKey(models.Model, on_delete=models.CASCADE)
    # source_type = source.__name__
