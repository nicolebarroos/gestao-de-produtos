from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido
from .actions import nfe_nao_emitida, nfe_emitida

class ItemPedidoInLine(admin.TabularInline):
    model = ItemDoPedido
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    list_filter = ('clientes__cpf', )
    list_display = ('numero', 'clientes', 'nfe_emitida', 'get_total')
    inlines = [ItemPedidoInLine]
    actions = [nfe_emitida, nfe_nao_emitida, ]

    def get_total(self, obj):
        return obj.calcular_total()

    get_total.short_description = 'Total'

admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)

