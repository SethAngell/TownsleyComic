from accounts.models import CustomUser, AboutPhotos
from django.shortcuts import render


def AboutView(request):
    user = CustomUser.objects.get(id=1)
    photos = AboutPhotos.objects.filter(user=1)

    simple_photos = []
    for photo in photos:
        simple_photos.append(
            {"url": photo.photo.image.url, "alt": photo.photo.alt_text}
        )

    context = {
        "user": user,
        "profile_picture": {"url": user.photo.image.url, "alt": user.photo.alt_text},
        "photos": simple_photos,
    }

    return render(request, "accounts/about.html", context)
