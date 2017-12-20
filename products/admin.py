from django.contrib import admin
from .models import Product

# Register your models here.
class DisplayProduct(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price')
    search_fields = ['name', 'brand']
    list_filter = ('brand', 'price')
    list_editable = ['price']
admin.site.register(Product, DisplayProduct)
