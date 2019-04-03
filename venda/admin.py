from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido
from .actions import nfe_nao_emitida, nfe_emitida

class ItemPedidoInLine(admin.TabularInline):
    model = ItemDoPedido
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('clientes__cpf', )
    list_display = ('numero', 'clientes', 'valor', 'nfe_emitida',)
    inlines = [ItemPedidoInLine]
    actions = [nfe_emitida, nfe_nao_emitida]

admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)

