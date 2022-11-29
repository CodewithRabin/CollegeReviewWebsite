from django import forms
from .models import *

# college add form
class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields =('name','address','description','image')