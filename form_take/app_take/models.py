from django.db import models


# Create your models here.
class registros(models.Model):
    id_usuario = models.AutoField(primary_key=True, serialize=False)
    nome = models.TextField(max_length=255, null=True)
    idade = models.IntegerField()
