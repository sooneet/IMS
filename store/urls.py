from django.urls import path
from . import views


urlpatterns = [
    path('create-supplier/',views.create_supplier,name='create-supplier'),
    path('supplier-list/',views.SupplierList.as_view(),name='supplier-list'),


    path('create-buyer/',views.create_buyer,name='create-buyer'),
    path('buyer-list/',views.BuyerList.as_view(),name='buyer-list'),


    path('create-product/',views.create_product,name='create-product'),
    path('product-list/',views.ProductList.as_view(),name='product-list'),

    path('create-order/',views.create_order,name='create-order'),
    path('order-list/',views.OrderList.as_view(),name='order-list'),    
]
