from django.contrib import admin
from content.models import ImageContent, FileContent


# Register your models here.
class ImageContentAdmin(admin.ModelAdmin):
    pass


class FileContentAdmin(admin.ModelAdmin):
    pass


admin.site.register(ImageContent, ImageContentAdmin)
admin.site.register(FileContent, FileContentAdmin)
