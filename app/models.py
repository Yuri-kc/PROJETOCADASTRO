from django.db import models

class PRODUTO(models.Model):
    NOME = models.CharField(max_length=50)
    COR = models.CharField(max_length=50)
    MATERIAL = models.CharField(max_length=30)
    QUANTIDADE = models.IntegerField()