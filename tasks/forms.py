# from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['tittle','description','important']
        widgets = {
            'tittle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write a title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }

