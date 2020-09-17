from django import forms
from .models import SubContent


class SubContentForm(forms.ModelForm):

    class Meta:
        model = SubContent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
