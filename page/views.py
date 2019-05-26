from django.shortcuts import render ,redirect
from . import forms
from .models import Bvn
import requests

# Create your views here.
'''def index(request):
    url = 'https://ravesandboxapi.flutterwave.com/v2/kyc/bvn/{}?seckey=FLWSECK-4d4e435aa173a758ea07fc9e48e824b7-X'
    bvn = 12345678901
    r = requests.get(url.format(bvn)).json()

    context = {
        "bvn": bvn,
        "first_name": r['data']['first_name'],
        "last_name":r['data']['last_name'],
        "date_of_birth":r['data']['date_of_birth'],
        "phone_number":r['data']['phone_number'],
    }
    print(context)
    return render(request, 'page/index.html', context)'''

'''class index(CreateView):
    template_name= 'bvn/bvn_create.html'
    form_class = forms.BvnForm
    print(form_class.cleaned_data)
    queryset = Bvn.objects.all()'''

'''def index(request):
    data_values = {}
    form = forms.BvnForm()
    if request.method == "POST":
        form = forms.BvnForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data
            url = 'https://ravesandboxapi.flutterwave.com/v2/kyc/bvn/{}?seckey=FLWSECK-4d4e435aa173a758ea07fc9e48e824b7-X'
            bvn = value['bvnumber']
            r = requests.get(url.format(bvn)).json()
            data_values = {
                "bvn": bvn,
                "first_name": r['data']['first_name'],
                "last_name":r['data']['last_name'],
                "date_of_birth":r['data']['date_of_birth'],
                "phone_number":r['data']['phone_number'],
            }
            return redirect('suc/')
            print(data_values)
            Bvn.objects.create(**form.cleaned_data)
        else: 
            print(form.errors)
    context = { 'form': form,
        'data_values' :data_values}
    return render(request, 'page/index.html', context)'''

def index(request):
    data_values = {}
    form = forms.BvnForm()
    if request.method == "POST":
        form = forms.BvnForm(request.POST)
        if form.is_valid():
            Bvn.objects.create(**form.cleaned_data)
            redirect('verification/successpage/')
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
    context = {
        'data_values' : data_values
    }
    return render(request, 'page/successpage.html', {})
    




