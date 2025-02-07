from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class ProductListView(ListView):
    model = Produto
    template_name = "home.html"
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Produto
    form_class = ProductForm
    template_name = "product-add.html"
    success_url = reverse_lazy('product')

class SupplierListView(ListView):
    model = Fornecedor
    template_name = "supplier.html"
    context_object_name = 'suppliers'

class SupplierCreateView(CreateView):
    model = Fornecedor
    form_class = SupplierForm
    template_name = "supplier-add.html"
    success_url = reverse_lazy('supplier')

class CategoryListView(ListView):
    model = Categoria
    template_name = "category.html"
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Categoria
    form_class = CategoryForm
    template_name = "category-add.html"
    success_url = reverse_lazy('category')