from django import forms
from django.forms import ModelForm
from.models import Menu
class MenuForm(forms.ModelForm):
     class Meta:
        model= Menu
        fields = '__all__'
       