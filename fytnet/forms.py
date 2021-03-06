from django import forms

from .models import Fighter, Discipline


class FighterForm(forms.ModelForm):
    class Meta:
        model = Fighter

        # change this to not include all fields -- only admin should

        fields = "__all__"

        # this excludes the below fields
        exclude = ("is_verified", "user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disciplines = Discipline.objects.all()
        friendly_names = [(d.id, d.get_friendly_name()) for d in disciplines]

        self.fields["discipline"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


def __init__(self, *args, **kwargs):
    super(FighterForm, self).__init__(*args, **kwargs)
