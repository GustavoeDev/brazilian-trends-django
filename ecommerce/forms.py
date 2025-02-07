from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome do produto deve ter pelo menos 3 caracteres.")
        return nome
    
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco <= 0:
            raise forms.ValidationError("O preço do produto deve ser maior que zero.")
        return preco
    
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade < 0:
            raise forms.ValidationError("A quantidade em estoque deve ser um número inteiro maior ou igual a zero.")
        return quantidade

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if not codigo.isalnum():
            raise forms.ValidationError("O código do produto deve conter apenas letras e números (sem espaços ou caracteres especiais).")
        return codigo