from django import forms
from django.contrib.auth.models import User

from .models import Trening


class AddTrening(forms.ModelForm):
    Nazwa_Treningu = forms.CharField(max_length=16)
    Data_Treningu = forms.DateField()
    Opis = forms.TextInput()
    CzasTreningu = forms.IntegerField()
    User = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Trening
        fields = ['Nazwa_Treningu', 'Data_Treningu', 'Opis', 'CzasTreningu', 'User']
