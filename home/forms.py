from django import forms
from .models import SubContent, Slides, MainContent, Contact


class SubContentForm(forms.ModelForm):

    class Meta:
        model = SubContent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
