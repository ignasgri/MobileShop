from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ebaylink = models.CharField(max_length=999, default='')
    image1 = models.ImageField(upload_to='images', blank=True, null=True)
    image2 = models.ImageField(upload_to='images', blank=True, null=True)
    image3 = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name