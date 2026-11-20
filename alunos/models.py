from django.db import models
class Aluno(models.Model):
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
# Create your models here.
