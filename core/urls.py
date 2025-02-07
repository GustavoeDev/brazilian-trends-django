from django.contrib import admin
from django.urls import path
from ecommerce.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='product'),
    path('produto/adicionar/', ProductCreateView.as_view(), name='product-add'),
]
