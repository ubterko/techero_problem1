
from django import forms
from .models import Bvn

class BvnForm(forms.Form):
	bvnumber = forms.CharField(max_length=20)