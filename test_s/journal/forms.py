from django import forms
from .models import Journal

class JournalForm(forms.Form):
    text = forms.CharField(max_length=200)

