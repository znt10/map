from django.db import models


class Artista(models.Model):
    nome = models.CharField(max_length=100)
    nome_artistic = models.CharField(max_length=100,blank=True, null=True) # Campo opcional
    tipo_arte = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='artistas/', blank=True, null=True)
    rede_social = models.URLField(blank=True)

    def __str__(self):
        return self.nome
    

class Perfil(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    

    def __str__(self):
        return self.email
