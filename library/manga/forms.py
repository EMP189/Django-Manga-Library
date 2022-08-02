from django import forms
from .models import Manga

class AddMangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields= ['name', 'read_status', 'chapter'] # fields must be the same as in the model we use