from django.db import models
from django.db.models import Sum, F, FloatField, Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from clientes.models import Cadastro
from produtos.models import Produto


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    clientes = models.ForeignKey(Cadastro, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('setar_nfe', 'Usuário pode alterar parâmetro NF-e'),
            ('permissão 2', 'Descrição da permissão 2'),
        )

    #Calculando o total do pedido com funções agregadas - Sum
    
    def calcular_total(self):
        tot = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] or 0 

        tot = tot - float(self.impostos) - float(self.desconto)
        self.valor = tot
        Venda.objects.filter(id=self.id).update(valor=tot)

    def __str__(self):
        return self.numero

class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self): #trazer o nome do object no admin de forma apresentável
        return self.venda.numero + ' - ' + self.produto.nome


    #django signals
#decorator(tipo de sinal, sender que vai percorrer todos os elementos de venda atraves do 'through')
@receiver(post_save, sender=ItemDoPedido) 
def update_vendas_total(sender, instance, **kwargs): #passamos esses elementos como padrão
    instance.venda.calcular_total()

@receiver(post_save, sender=Venda)
def update_vendas_total2(sender, instance, **kwargs): #passamos esses elementos como padrão
    instance.calcular_total()