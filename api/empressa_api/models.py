from django.db import models


# Create your models here.
class Empressa(models.Model):
    nome_empressa = models.CharField(max_length= 2000)
    endereco = models.CharField(max_length= 2000)
    numero= models.CharField(max_length=2000) 
    mail = models.CharField(max_length= 2000)
    contato = models.CharField(max_length= 2000)
    avalicao = models.IntegerField(default=0)


    def __str__(self):
        return self.nome_empressa