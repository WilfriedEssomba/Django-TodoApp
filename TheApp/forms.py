from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(required=False)
    
    class Meta:
        model = Task
        fields = ['title', 'completed']