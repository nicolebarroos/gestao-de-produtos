from django.db import models
from clientes.models import Cadastro
from produtos.models import Produto

class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    clientes = models.ForeignKey(Cadastro, null=True, blank=True, on_delete=models.PROTECT)
    #nfe_emitida = models.BooleanField(default=False)

    def __str__(self):
        return self.numero

class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self): #trazer o nome do object no admin de forma apresentável
        return self.venda.numero + ' - ' + self.produto.descricao