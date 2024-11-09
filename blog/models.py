from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()  # Armazena conteúdo HTML
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo