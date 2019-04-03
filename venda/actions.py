from django.http import HttpResponseNotFound

def nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('venda.setar_nfe'):
        queryset.update(nfe_emitida='True')
    else:
        return HttpResponseNotFound('<h6>Sem Permissão</h6>')


nfe_emitida.short_description = "NF-e emitida"

def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_nao_emitida='False')

nfe_nao_emitida.short_description = "NF-e não emitida"