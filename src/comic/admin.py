from django.contrib import admin
from comic.models import Project, Volume, Scene, Page


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass


class VolumeAdmin(admin.ModelAdmin):
    pass


class SceneAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(Scene, SceneAdmin)
admin.site.register(Page, PageAdmin)
