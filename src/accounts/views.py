from accounts.models import CustomUser
from django.shortcuts import render


def AboutView(request):
    user = CustomUser.objects.get(id=1)

    context = {
        "user": user,
        "profile_picture": {"url": user.photo.image.url, "alt": user.photo.alt_text},
    }

    print(context["user"].photo.image.url)
    print(request.META["REMOTE_ADDR"])

    return render(request, "accounts/about.html", context)
