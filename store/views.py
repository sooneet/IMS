from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . forms import SupplierForm
from . models import Supplier,User

# Create your views here.
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()

    if request.method == 'POST':
        forms = SupplierForm(request.POST)

        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            username = forms.cleaned_data['username']
            email = forms.cleaned_data['email']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']   

            if password == retype_password:
                user =  User.objects.create(username=username,
                                            email=email,
                                            password=password,
                                            is_supplier=True)

                Supplier.objects.create(user=user,name=name,address=address)   
                return HttpResponse('<h2>supplier created</h2>')      
                                          
    return render(request,'store/create_supplier.html',{'form':forms})