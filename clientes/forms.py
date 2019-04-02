from django.forms import ModelForm
from .models import Cadastro


class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereço', 'doc']
