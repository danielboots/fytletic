from django import forms
from .widgets import CustomClearableFileInput
from .models import Fighter, Discipline


class FighterForm(forms.ModelForm):
    class Meta:
        model = Fighter
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disciplines = Discipline.objects.all()
        friendly_names = [(d.id, d.get_friendly_name()) for d in disciplines]

        self.fields["discipline"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
