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



