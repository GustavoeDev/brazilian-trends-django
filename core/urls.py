from django.contrib import admin
from django.urls import path
from ecommerce.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='product'),
    path('produto/adicionar/', ProductCreateView.as_view(), name='product-add'),
    path('fornecedor/', SupplierListView.as_view(), name='supplier'),
    path('fornecedor/adicionar/', SupplierCreateView.as_view(), name='supplier-add'),
]
