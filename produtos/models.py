from django.db import models

#Definição dos campos do produto

class Codigo (models.Model):
    num_cod = models.CharField( max_length = 50 )

    def  __str__ (self):
        return self.num_cod


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    marca = models.CharField(max_length=30)
    cod = models.OneToOneField(Codigo, null=True, blank=True, on_delete=models.CASCADE)

class Compra(models.Model):
    protocolo = models.CharField(max_length=5, blank=True, null=True)
    data_hora = models.DateTimeField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.protocolo

class Pessoas(models.Model):
    nome = models.CharField(max_length=30)
    Produto = models.ForeignKey(Produto, null=True, blank=False, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    endereço = models.CharField(max_length=120)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data = models.DateField('DD-MM-YYYY')
    compra = models.ManyToManyField(Compra, blank=True)

    def __str__(self):
        return self.nome

