from django.http import HttpResponse
from django.shortcuts import redirect, render
from . forms import LoginForm
from django.contrib.auth import authenticate,login,logout


# Create your views her
def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponse('<h2>login</h2>')
    return render(request,'users/login.html',{'form':forms})


def logout_page(request):
    logout(request)
    return redirect('login')