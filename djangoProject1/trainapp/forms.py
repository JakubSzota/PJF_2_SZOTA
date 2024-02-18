from django import forms
from django.forms import inlineformset_factory

from .models import Training, TrainingExercise


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['name', 'datetime', 'executed', 'user', 'description']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

class TrainingExerciseForm(forms.ModelForm):
    class Meta:
        model = TrainingExercise
        fields = ['exercise', 'repetitions', 'series']