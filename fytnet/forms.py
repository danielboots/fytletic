from django import forms
from .widgets import CustomClearableFileInput
from .models import Fighter, Discipline
from gym.models import Gym, GymType


class FighterForm(forms.ModelForm):
    class Meta:
        model = Fighter
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    gyms = forms.ModelChoiceField(
        queryset=Gym.objects.all(), empty_label="No selection"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        gym_type = GymType.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in gym_type]

        self.fields["discipline"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
