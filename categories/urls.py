from django.conf.urls import url
from .views import root_categories, get_category
from home.views import no_product

urlpatterns = [
    url(r'^$', root_categories, name='categories'),
    url(r'^(?P<id>\d+)$', get_category, name='category'),
    url(r'^noproduct$', no_product, name='no_product'),
]