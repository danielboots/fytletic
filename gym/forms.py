from django import forms
from .widgets import CustomClearableFileInput
from .models import Gym, GymType


class GymForm(forms.ModelForm):
    class Meta:
        model = Gym

        # change this to not include all fields -- only admin should

        fields = "__all__"

        # this excludes the below fields
        exclude = ("is_verified",)

    # "gym"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        gymtype = gymType.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in gymtype]

        self.fields["gymtype"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


def __init__(self, *args, **kwargs):
    super(GymForm, self).__init__(*args, **kwargs)