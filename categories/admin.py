from django.contrib import admin
from .models import Category

# Register your models here.

class DisplayCategory(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ['name']
    list_filter = ('name',)
admin.site.register(Category, DisplayCategory)

# admin.site.register(Category)