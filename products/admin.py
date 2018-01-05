from django.contrib import admin
from .models import Product
from django.forms import TextInput
from django.db import models

# Register your models here.
class DisplayProduct(admin.ModelAdmin):
    list_display = ('brand', 'name', 'price', 'published_date')
    search_fields = ['name', 'brand']
    list_filter = ('brand', 'price')
    list_editable = ['price']

    # formfield_overrides = {
    #     # Django enforces maximum field length of 14 onto 'title' field when user is editing in the change form
    #     models.DecimalField: {'widget': TextInput(attrs={'size':'5'})},
    #     }

admin.site.register(Product, DisplayProduct)
