from django import forms
from .models import Img


class ImgForm(forms.ModelForm):

    class Meta:
        model = Img
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
