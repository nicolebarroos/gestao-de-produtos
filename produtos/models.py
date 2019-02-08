from django.db import models

#Definição dos campos do produto

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    marca = models.CharField(max_length=30)
