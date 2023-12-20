from comic.models import Project, Volume, Scene, Page
from content.models import ImageContent
from config.models import ConfigObject
from django.shortcuts import render
from comic.forms import ProjectForm, VolumeForm, SceneForm
from django.http import HttpResponseRedirect


from uuid import uuid4


def HomeView(request):
    displayed_project = int(ConfigObject.objects.get(key="CURRENT_PROJECT").value)
    project = Project.objects.get(id=displayed_project)
    volumes = Volume.objects.filter(project=project.id).order_by("order")
    scenes = Scene.objects.filter(volume__in=[volume.id for volume in volumes])
    pages = Page.objects.filter(scene__in=[scene.id for scene in scenes])

    projectPayload = _generate_project_payload(project, volumes, scenes, pages)

    context = {"project": projectPayload, "home": True}

    return render(request, "comic/comic.html", context)


def ComicView(request):
    displayed_project = int(ConfigObject.objects.get(key="CURRENT_PROJECT").value)
    project = Project.objects.get(id=displayed_project)
    volumes = Volume.objects.filter(project=project.id).order_by("order")
    scenes = Scene.objects.filter(volume__in=[volume.id for volume in volumes])
    pages = Page.objects.filter(scene__in=[scene.id for scene in scenes])

    projectPayload = _generate_project_payload(project, volumes, scenes, pages)

    context = {"project": projectPayload, "home": False}

    return render(request, "comic/comic.html", context)


def ProjectIndexView(request):
    projects = Project.objects.all()
    context = {"projects": projects}

    return render(request, "comic/project/index.html", context)


def ProjectDetailView(request, id):
    project = Project.objects.get(id=id)
    context = {"project": project}

    return render(request, "comic/project/detail.html", context)


def ProjectEditView(request, id):
    project = Project.objects.get(id=id)

    if request.method == "GET":
        images = ImageContent.objects.all()
        context = {"project": project, "image_options": images}

        return render(request, "comic/project/edit.html", context)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            project.name = form.cleaned_data["name"]
            project.description = form.cleaned_data["description"]
            project.image = form.cleaned_data["image"]
            project.save()
            return HttpResponseRedirect(f"/comic/project/{id}/")


def ProjectCreateView(request):
    if request.method == "GET":
        images = ImageContent.objects.all()
        context = {"image_options": images}

        return render(request, "comic/project/create.html", context)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            project = Project(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                image=form.cleaned_data["image"],
            )

            project.save()
            return HttpResponseRedirect(f"/comic/project/{id}/")


def VolumeIndexView(request):
    volumes = Volume.objects.all()
    context = {"volumes": volumes}

    return render(request, "comic/volume/index.html", context)


def VolumeDetailView(request, id):
    volume = Volume.objects.get(id=id)
    scenes = Scene.objects.filter(volume=volume)
    context = {"volume": volume, "scene_count": len(scenes), "scenes": scenes}

    return render(request, "comic/volume/detail.html", context)


def VolumeEditView(request, id):
    volume = Volume.objects.get(id=id)
    projects = Project.objects.all()

    if request.method == "GET":
        context = {"volume": volume, "projects": projects}

        return render(request, "comic/volume/edit.html", context)
    if request.method == "POST":
        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = VolumeForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            volume.name = form.cleaned_data["name"]
            volume.order = form.cleaned_data["order"]
            volume.project = form.cleaned_data["project"]
            volume.save()
            return HttpResponseRedirect(f"/comic/volume/{id}/")


def VolumeCreateView(request):
    projects = Project.objects.all()

    if request.method == "GET":
        context = {"projects": projects}

        return render(request, "comic/volume/create.html", context)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = VolumeForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            volume = Volume(
                name=form.cleaned_data["name"],
                order=form.cleaned_data["order"],
                project=form.cleaned_data["project"],
            )
            volume.save()
            return HttpResponseRedirect(f"/comic/volume/{id}/")


def SceneDetailView(request, id):
    scene = Scene.objects.get(id=id)
    pages = Page.objects.filter(scene=scene)

    context = {"scene": scene, "pages": pages, "page_count": len(pages)}

    return render(request, "comic/scene/detail.html", context)


def SceneEditView(request, id):
    scene = Scene.objects.get(id=id)
    pages = Page.objects.all()
    volumes = Volume.objects.all()
    premarked_pages = [
        {"selected": page.scene == scene, "page": page} for page in pages
    ]

    if request.method == "GET":
        context = {"scene": scene, "pages": premarked_pages, "volumes": volumes}

        return render(request, "comic/scene/edit.html", context)
    if request.method == "POST":
        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = VolumeForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            volume.name = form.cleaned_data["name"]
            volume.order = form.cleaned_data["order"]
            volume.project = form.cleaned_data["project"]
            volume.save()
            return HttpResponseRedirect(f"/comic/volume/{id}/")


def _generate_project_payload(project, volumes, scenes, pages):
    projectPayload = {
        "name": project.name,
        "description": project.description,
        "image_url": project.image.image.url,
        "volumes": [],
        "pageArray": [],
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
                projectPayload["pageArray"].append(
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
