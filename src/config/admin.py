from django.contrib import admin
from config.models import ConfigObject, FeatureFlag


# Register your models here.
class ConfigObjectAdmin(admin.ModelAdmin):
    pass


class FeatureFlagAdmin(admin.ModelAdmin):
    pass


admin.site.register(ConfigObject, ConfigObjectAdmin)
admin.site.register(FeatureFlag, FeatureFlagAdmin)
