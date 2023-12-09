from content.models import ImageContent
from django.forms import ModelForm


class ImageContentForm(ModelForm):
    class Meta:
        model = ImageContent
        fields = ["name", "alt_text", "image"]
