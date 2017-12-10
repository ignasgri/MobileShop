from django.conf.urls import url
from .views import *
from .import views

urlpatterns = [
    url(r'^$', all_products, name='products'),
]