from accounts.views import AboutView

from django.urls import path

# api_urlpatterns = [
#     path("user/", api_create_custom_user),
#     path("user/info/", api_get_current_user_info),
# ]

static_url_patterns = [path("about/", AboutView)]
