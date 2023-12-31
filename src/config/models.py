from django.db import models


# Create your models here.
class ConfigObject(models.Model):
    key = models.CharField(max_length=32)
    value = models.CharField(max_length=1024)

    def __str__(self):
        return self.key


class FeatureFlag(models.Model):
    key = models.CharField(max_length=32)
    value = models.BooleanField(verbose_name="Feature Enabled", default=False)

    def __str__(self):
        return f"{self.key}: {self.value}"
