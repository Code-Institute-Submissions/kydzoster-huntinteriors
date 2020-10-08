from django import forms
from .models import Services


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
