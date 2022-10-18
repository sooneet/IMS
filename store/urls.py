from django.urls import path
from . import views


urlpatterns = [
    path('create-supplier/',views.create_supplier,name='create-supplier'),
    path('supplier-list/',views.SupplierList.as_view(),name='supplier-list'),
]
