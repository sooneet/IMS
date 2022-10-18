from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Buyer,Supplier,Order,Product

@login_required(login_url='login')    
def dashboard(request):
    total_buyer = Buyer.objects.all().count
    total_supplier = Supplier.objects.all().count
    total_order = Order.objects.all().count
    total_product = Product.objects.all().count
    orders = Order.objects.all().order_by('-id')
    return render(request,'dashboard.html')