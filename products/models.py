from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.forms import TextInput, Textarea
from categories.models import Category


Condition = (
    ('New', 'New'),
    ('Used', 'Used'),

)
class Product(models.Model):
    brand = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=254, default='')
    category = models.ManyToManyField(Category)
    condition = models.CharField(max_length=4, choices=Condition, default='New')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    ebaylink = models.CharField(max_length=999, default='')
    image1 = models.ImageField(upload_to='images', blank=True, null=True)
    image2 = models.ImageField(upload_to='images', blank=True, null=True)
    image3 = models.ImageField(upload_to='images', blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    