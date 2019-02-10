from django.forms import ModelForm
from .models import Produto
from django.contrib.auth import get_user_model

#Criar um formulário pegando os campos do model

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'preco', 'marca']
    