from django import forms
from .models import Slides, MainContent


class SlidesForm(forms.ModelForm):

    class Meta:
        model = Slides
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TitleForm(forms.ModelForm):

    class Meta:
        model = MainContent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def empty_field(value):
    if value:
        raise forms.ValidationError('Field must be empty')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    # targets bots
    nobotsallowed = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave Empty",
        validators=[empty_field]
    )
