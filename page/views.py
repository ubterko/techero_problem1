from django.shortcuts import render ,redirect
from . import forms
from .models import Bvn
import requests

def index(request):
    data_values = {}
    form = forms.BvnForm()
    if request.method == "POST":
        form = forms.BvnForm(request.POST)
        if form.is_valid():
            Bvn.objects.create(**form.cleaned_data)
            return redirect('verification/success/')
        else:
            print(form.errors)
    context = { 'form': form}
    return render(request, 'page/index.html', context)


def successpage(request):
    value = Bvn.objects.latest('id')
    url = 'https://ravesandboxapi.flutterwave.com/v2/kyc/bvn/{}?seckey=FLWSECK-4d4e435aa173a758ea07fc9e48e824b7-X'
    bvn = value
    r = requests.get(url.format(bvn)).json()
    data_values = {
        "bvn": bvn,
        "first_name": r['data']['first_name'],
        "last_name":r['data']['last_name'],
        "date_of_birth":r['data']['date_of_birth'],
        "phone_number":r['data']['phone_number'],
    }
    print(data_values['first_name'])
    context = {
        'data_values' : data_values
    }
    return render(request, 'page/successpage.html', {})
    




