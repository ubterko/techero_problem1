
from django import forms
from .models import Bvn

'''class BvnForm(forms.ModelForm):
    class Meta:
        model = Bvn
        fields = ['bvnumber']'''

class BvnForm(forms.Form):
	bvnumber = forms.CharField(max_length=20)