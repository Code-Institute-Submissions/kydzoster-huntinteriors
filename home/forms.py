from django import forms
from .models import MainContent, SubContent


class TitleForm(forms.ModelForm):

    class Meta:
        model = MainContent
        fields = '__all__'


class SubContentForm(forms.ModelForm):

    class Meta:
        model = SubContent
        fields = '__all__'
