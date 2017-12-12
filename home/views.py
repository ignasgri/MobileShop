from django.shortcuts import render
from products.models import Product

def get_index(request):
    # products = Product.object.all()
    return render(request, 'index.html')
    # return render(request, 'index.html', {"products": products})

