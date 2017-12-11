from django.shortcuts import render, get_list_or_404
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    args = {}
    args.update(csrf(request))
    return render(request, "products.html", {"products": products}, args)




class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer