from django.contrib import admin
from django.urls import path
from ecommerce.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('produto/', ProductListView.as_view(), name='product'),
    path('produto/adicionar/', ProductCreateView.as_view(), name='product-add'),
    path('fornecedor/', SupplierListView.as_view(), name='supplier'),
    path('fornecedor/adicionar/', SupplierCreateView.as_view(), name='supplier-add'),
    path('categoria/', CategoryListView.as_view(), name='category'),
    path('categoria/adicionar/', CategoryCreateView.as_view(), name='category-add'),
]
