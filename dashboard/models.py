from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# admin
# admin@123
# vaibhav@123
# Ritika@123
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length = 100, null = True)
    category = models.CharField(max_length = 20, choices = CATEGORY, null = True)
    quantity = models.PositiveIntegerField(null = True)

    class Meta:
        verbose_name_plural = 'staff'

    def __str__(self):
        return f'{self.name} {self.quantity}'

class Order(models.Model):
    Product = models.ForeignKey(Product,on_delete = models.CASCADE, null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    Order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product } ordered by { self.staff.username}'
