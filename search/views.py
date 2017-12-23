from django.shortcuts import render, get_object_or_404
from products.models import Product
from rest_framework import viewsets
from products.serializers import ProductSerializer
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
# def do_search(request):
#     products = Product.objects.filter(name__contains=request.GET['search'])
#     return render(request, 'results.html', {'products':products})


# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__contains=request.GET['search'])
    # products = Product.objects.filter(brand__contains=request.GET['search'])
    # products = Product.objects.filter(description__contains=request.GET['search'])

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    args = {}
    args.update(csrf(request))
    return render(request, "results.html", {"products": products}, args)




class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer