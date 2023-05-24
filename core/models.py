from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.IntegerField()

    def __str__(self) -> str:
        return self.nome