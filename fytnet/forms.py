from django import forms
from .widgets import CustomClearableFileInput
from .models import Fighter, Category
from gym.models import Gym


class FighterForm(forms.ModelForm):
    class Meta:
        model = Fighter
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    gyms = forms.ModelChoiceField(queryset=Gym.objects.all(), empty_label="No Gyms Yet")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
