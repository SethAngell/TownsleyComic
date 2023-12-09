from django.shortcuts import render
from content.models import ImageContent
from content.forms import ImageContentForm
from django.http import HttpResponseRedirect


# Create your views here.
def ImageIndexView(request):
    images = ImageContent.objects.filter(user=request.user)
    context = {"images": images}

    return render(request, "content/image_index.html", context)


def ImageDetailView(request, id):
    image = ImageContent.objects.get(id=id)
    context = {"image": image}

    return render(request, "content/image_detail.html", context)


def ImageEditView(request, id):
    if request.method == "GET":
        image = ImageContent.objects.get(id=id)
        context = {"image": image}

        return render(request, "content/image_edit.html", context)
    elif request.method == "POST":
        image = ImageContent.objects.get(id=id)
        print(request.POST)
        print(request)

        # create a form instance and populate it with data from the request:
        form = ImageContentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            image.name = form.cleaned_data["name"]
            image.alt_text = form.cleaned_data["alt_text"]
            if form.cleaned_data["image"] != None:
                image.image = form.cleaned_data["image"]
            image.save()
            return HttpResponseRedirect(f"/content/image_detail/{id}/")


def ImageCreateView(request):
    if request.method == "GET":
        return render(request, "content/image_create.html", {})
    elif request.method == "POST":
        print(request.POST)
        print(request)

        # create a form instance and populate it with data from the request:
        form = ImageContentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            image = ImageContent(
                name=form.cleaned_data["name"],
                alt_text=form.cleaned_data["alt_text"],
                user=request.user,
                image=form.cleaned_data["image"],
            )
            image.save()

            return HttpResponseRedirect(f"/content/image_detail/{image.id}/")
