from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido

class ItemPedidoInLine(admin.TabularInline):
    model = ItemDoPedido
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('clientes__doc', )
    inlines = [ItemPedidoInLine]

admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)

