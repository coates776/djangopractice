from django import forms
from django.forms import ModelForm
from .models import Place


class PlaceForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Place
        fields = '__all__'
