from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default='')
    image = models.ImageField(upload_to='products_images')
    size = models.PositiveIntegerField(default='')
    def __str__(self):
        return f'Продукт: {self.name}'