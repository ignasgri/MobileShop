from django.shortcuts import render, get_list_or_404
from products.models import Product
from rest_framework import viewsets
from django.utils import timezone
from products.serializers import ProductSerializer
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def get_index(request):
#     products = Product.objects.all()
#     # return render(request, 'index.html')
#     return render(request, 'index.html', {"products": products})

# Create your views here.
# def get_index(request):
#     products = Product.objects.all()
#     paginator = Paginator(products, 6)
#     page = request.GET.get('page')
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)
#     args = {}
#     args.update(csrf(request))
#     return render(request, "index.html", {"products": products}, args)

# class ProductViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
def no_product(request):
    products = Product.objects.all()
    return render(request, 'noproduct.html')



def latest_products(request):
    products = Product.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')[0:999]
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    args = {}
    args.update(csrf(request))
    return render(request, "index.html", {'products': products})
class ProductViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer