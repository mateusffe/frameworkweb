import unicodedata
from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    nome_limpo = models.CharField(max_length=255, editable=False)  
    profissao = models.CharField(max_length=255)
    empresa_ligada = models.CharField(max_length=255, blank=True)
    descricao = models.CharField(max_length=500, blank=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.nome_limpo = ''.join(
            c for c in unicodedata.normalize('NFD', self.nome) if unicodedata.category(c) != 'Mn'
        ).lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome