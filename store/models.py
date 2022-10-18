from django.db import models

from users.models import User

# Create your models here.
class Supplier(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120,unique=True)
    address = models.CharField(max_length=120)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120,unique=True)
    address = models.CharField(max_length=120)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120,unique=True)
    sortno = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name      


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending','pending'),
        ('decline','decline'),
        ('approved','approved'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name    


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    curier_name = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.curier_name               