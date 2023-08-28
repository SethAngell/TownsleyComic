from django.contrib import admin
from config.models import ConfigObject


# Register your models here.
class ConfigObjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(ConfigObject, ConfigObjectAdmin)
