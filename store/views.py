from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from . forms import OrderForm, ProductForm, SupplierForm,BuyerForm
from . models import Product, Supplier, Buyer, Order, User

# Create your views here.

class OrderList(ListView):
    model = Product
    template_name = 'store/order_list.html'
    context_object_name = 'order'


@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()

    if request.method == 'POST':
        forms = OrderForm(request.POST)

        if forms.is_valid():
            buyer = forms.cleaned_data['buyer']
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']

            Order.objects.create(buyer=buyer,supplier=supplier,product=product,status='pending')

            return HttpResponse('<h2>order-list</h2>')

    return render(request,'store/create_order.html',{'form':forms})


class ProductList(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()

    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')

    return render(request,'store/create_product.html',{'form':forms})

class BuyerList(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'


@login_required(login_url='login')
def create_buyer(request):
    forms = BuyerForm()

    if request.method == 'POST':
        forms = BuyerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            address = forms.cleaned_data['address']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']

            if password == retype_password:
                user = User.objects.create(username=username,password=password,email=email,is_buyer=True)

                Buyer.objects.create(user=user,name=name,address=address)
                return HttpResponse('<h2>create-buyer</h2>')
    return render(request,'store/create_buyer.html',{'form':forms})


class SupplierList(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


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
                return redirect('supplier-list')      

    return render(request,'store/create_supplier.html',{'form':forms})


