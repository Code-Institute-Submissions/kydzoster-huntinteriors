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
