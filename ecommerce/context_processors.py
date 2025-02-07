from .models import Categoria

def categories_context(request):
    categorias = Categoria.objects.all()
    return {"categorias": categorias}