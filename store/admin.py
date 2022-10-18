from django.contrib import admin

from . models import *
# Register your models here.

class BuyerAdmin(admin.ModelAdmin):
    list_display = ['name','address','created_at']


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name','address','created_at']

admin.site.register(Buyer,BuyerAdmin)    
admin.site.register(Supplier,SupplierAdmin)    
admin.site.register(Order)    
admin.site.register(Product)    
admin.site.register(Delivery)    
