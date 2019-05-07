from django import forms
from . import models

class CreateUser(forms.ModelForm):
    class Meta:
        model=models.Bill
        fields=['name','medi','qty','total']