from accounts.models import CustomUser, AboutPhotos
from config.models import ConfigObject
from django.shortcuts import render


def AboutView(request):
    current_author = int(ConfigObject.objects.get(key="CURRENT_AUTHOR").value)
    user = CustomUser.objects.get(id=current_author)
    photos = AboutPhotos.objects.filter(user=current_author)

    simple_photos = []
    for photo in photos:
        simple_photos.append(
            {"url": photo.photo.image.url, "alt": photo.photo.alt_text}
        )

    context = {
        "user": user,
        "profile_picture": {"url": user.photo.image.url, "alt": user.photo.alt_text},
        "about_photos_exist": len(simple_photos) != 0,
        "photos": simple_photos,
    }

    return render(request, "accounts/about.html", context)
