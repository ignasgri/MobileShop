from django.conf.urls import url, include
from django.contrib import admin
from home.views import latest_products
from products import urls as products_urls
from categories import urls as categories_urls
from django.views import static
from .settings import MEDIA_ROOT
from rest_framework import routers
from products import views as product_views
from search import urls as search_urls


router = routers.DefaultRouter()
router.register(r'products', product_views.ProductViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include(products_urls)),
    url(r'^categories/', include(categories_urls)),
    # url(r'^$', get_index, name='index'),
    url(r'^$', latest_products, name='index'),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^search/', include(search_urls)),
    
]
