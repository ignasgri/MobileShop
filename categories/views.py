from django.shortcuts import render, get_object_or_404
from .models import Category
from products.models import Product
from rest_framework import viewsets
from django.utils import timezone
from products.serializers import ProductSerializer
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def root_categories(request):
    categories = Category.objects.filter(parent=None)
    products = Product.objects.all().order_by('-published_date')[0:999]
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    args = { 'categories': categories, 'subcategories': {}, 'products': products}
    return render(request, 'categories.html', args)


def get_category(request, id):
    this_category = get_object_or_404(Category, pk=id)
    # root_categories = Category.object.filter(parent=None)
    crumbs = []
    crumb = this_category
    
    while crumb != None:
        crumbs.insert(0, crumb)
        crumb = crumb.parent

    subcategories = Category.objects.filter(parent=this_category)
    products = Product.objects.filter(category__in=[this_category]).order_by('-published_date')[0:999]
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    args = { 'categories': subcategories, 'products': products, 'crumbs': crumbs}
    return render(request, 'categories.html', args)


def root_categories_context(request):
    categories = Category.objects.filter(parent=None)
    category_tree = {}
    for category in categories:
        sub_categories = Category.objects.filter(parent=category)
        category_tree[category] = sub_categories
    return {'root_categories': category_tree}

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer