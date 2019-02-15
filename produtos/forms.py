from django.forms import ModelForm
from .models import Produto


#Criar um formulário pegando os campos do model

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'preco', 'marca']
    