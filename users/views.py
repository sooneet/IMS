from urllib import request
from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,'users/login.html')