from django.contrib import admin
from .models import Cadastro, Documento

class CadastroAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields':('nome', 'sobrenome', 'cpf', 'doc', 'telefone')}),
        ('Dados complementares', {'fields':('email', 'endereço')})
    )

admin.site.register(Cadastro, CadastroAdmin)
admin.site.register(Documento)
