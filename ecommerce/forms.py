from django import forms
from .models import Produto

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        nome = cleaned_data.get('nome')
        preco = cleaned_data.get('preco')
        quantidade = cleaned_data.get('quantidade')
        codigo = cleaned_data.get('codigo')

        if nome and len(nome) < 3:
            self.add_error('nome', "O nome do produto deve ter pelo menos 3 caracteres.")

        if preco is not None and preco <= 0:
            self.add_error('preco', "O preço do produto deve ser maior que zero.")

        if quantidade is not None and quantidade < 0:
            self.add_error('quantidade', "A quantidade em estoque deve ser um número inteiro maior ou igual a zero.")

        if codigo:
            if not codigo.isalnum():
                self.add_error('codigo', "O código do produto deve conter apenas letras e números (sem espaços ou caracteres especiais).")
            if Produto.objects.filter(codigo=codigo).exists():
                self.add_error('codigo', "Já existe um produto com esse código.")

        return cleaned_data
