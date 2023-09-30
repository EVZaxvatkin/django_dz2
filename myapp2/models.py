from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=50)
    data_registration = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    data_newproduct = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)











