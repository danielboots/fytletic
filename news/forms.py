from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]

    # user signed in user name for return
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
