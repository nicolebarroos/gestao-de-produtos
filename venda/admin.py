from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido

class ItemPedidoInLine(admin.TabularInline):
    model = ItemDoPedido
    extra = 1
   

admin.site.register(Venda)
admin.site.register(ItemDoPedido)
