from django import forms
from .models import *


class OfficeCreationForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    name = forms.CharField(max_length=100, label = "Office_Name")
    
    class Meta:
        model = Office
        fields = '__all__'

