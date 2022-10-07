from django import forms
from .models import RegstrationModel


class Regstaration(forms.ModelForm):
    class Meta:
        model = RegstrationModel
        fields = '__all__'