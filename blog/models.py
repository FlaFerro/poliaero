from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()  # Armazena conteúdo HTML
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.author} on {self.created_date}'
