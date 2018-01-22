from django.conf.urls import url
from .views import all_products
from home.views import no_product
from .import views


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^noproduct$', no_product, name='no_product'),
]