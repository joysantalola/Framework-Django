from django import forms
from .models import Anime, Personatge

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'

class PersonatgeForm(forms.ModelForm):
    class Meta:
        model = Personatge
        fields = '__all__'
#Oleguer
