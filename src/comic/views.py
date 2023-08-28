from comic.models import Project, Volume, Scene, Page
from config.models import ConfigObject
from django.shortcuts import render


def HomeView(request):
    displayed_project = int(ConfigObject.objects.get(key="CURRENT_PROJECT").value)
    project = Project.objects.get(id=displayed_project)
    volumes = Volume.objects.filter(project=project.id).order_by("order")
    scenes = Scene.objects.filter(volume__in=[volume.id for volume in volumes])
    pages = Page.objects.filter(scene__in=[scene.id for scene in scenes])

    projectPayload = _generate_project_payload(project, volumes, scenes, pages)

    context = {"project": projectPayload}

    return render(request, "comic/home.html", context)


def ComicView(request):
    displayed_project = int(ConfigObject.objects.get(key="CURRENT_PROJECT").value)
    project = Project.objects.get(id=displayed_project)
    volumes = Volume.objects.filter(project=project.id).order_by("order")
    scenes = Scene.objects.filter(volume__in=[volume.id for volume in volumes])
    pages = Page.objects.filter(scene__in=[scene.id for scene in scenes])

    projectPayload = _generate_project_payload(project, volumes, scenes, pages)

    context = {"project": projectPayload}

    return render(request, "comic/comic.html", context)


def _generate_project_payload(project, volumes, scenes, pages):
    projectPayload = {
        "name": project.name,
        "description": project.description,
        "volumes": [],
    }
    for volume in volumes:
        volumePayload = {"id": volume.id, "name": volume.name, "scenes": []}
        scenes_to_add = _get_scenes_for_volume(scenes, volume.id)
        scenes_to_add.sort(key=lambda x: x.number)

        for scene in scenes_to_add:
            current_scene = []
            pages_to_add = _get_pages_for_scene(pages, scene.id)
            for page in pages_to_add:
                current_scene.append(
                    {"url": page.content.image.url, "alt": page.content.alt_text}
                )

            volumePayload["scenes"].append(
                {"id": scene.id, "name": scene.name, "pages": current_scene}
            )

        projectPayload["volumes"].append(volumePayload)

    return projectPayload


def _get_pages_for_scene(page_list, scene_id):
    return [page for page in page_list if page.scene.id == scene_id]


def _get_scenes_for_volume(scene_list, volume_id):
    return [scene for scene in scene_list if scene.volume.id == volume_id]
