from django import forms
from .models import *



class OfficeTaskForm(forms.Form):
    office = forms.ModelChoiceField(queryset=Office.objects.all())
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    deadline = forms.DateTimeField()

    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        if deadline < datetime.now():
            raise forms.ValidationError('Deadline can not be in the past')
        return deadline
    
class TeamTaskForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    deadline = forms.DateTimeField()
    office_task = forms.ModelChoiceField(queryset=OfficeTask.objects.all(), required=False)

    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        if deadline < datetime.now():
            raise forms.ValidationError('Deadline can not be in the past')
        return deadline
    

class PersonalTaskForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    deadline = forms.DateTimeField()
    team_task = forms.ModelChoiceField(queryset=TeamTask.objects.all(), required=False)

    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        if deadline < datetime.now():
            raise forms.ValidationError('Deadline can not be in the past')
        return deadline

