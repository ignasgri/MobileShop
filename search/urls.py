from django.conf.urls import url
from django.contrib import admin
from .views import do_search
from home.views import no_product

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^noproduct$', no_product, name='no_product'),
    # url(r'^(/?search=\d+)$', get_search, name='get_search'),
]