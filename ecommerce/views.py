from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import *

class ProductListView(ListView):
    model = Produto
    template_name = "home.html"
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Produto
    form_class = ProductForm
    template_name = "product-add.html"
    success_url = reverse_lazy('home')