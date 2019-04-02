from django.db import models

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Cadastro(models.Model):
    nome = models.CharField(max_length=35)
    sobrenome = models.CharField(max_length=30)
    #idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    endereço = models.CharField(max_length=40)
    #salario = models.DecimalField(max_digits=5, decimal_places=2)
    #bio = models.TextField()
    #photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

