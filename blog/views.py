from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Listar todos os posts
class ListarPostsView(ListView):
    model = Post
    template_name = 'blog/listar_posts.html'
    context_object_name = 'posts'  # Nome da variável para acessar no template

# Detalhar um post específico
class DetalhesPostView(DetailView):
    model = Post
    template_name = 'blog/detalhes_post.html'
    context_object_name = 'post'  # Nome da variável para acessar no template

# Criar um novo post
class CriarPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form_post.html'
    success_url = reverse_lazy('listar_posts')  # Redireciona para a lista de posts após criar

# Editar um post existente
class EditarPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form_post.html'
    success_url = reverse_lazy('listar_posts')

# Deletar um post
class DeletarPostView(DeleteView):
    model = Post
    template_name = 'blog/confirmar_delecao.html'
    success_url = reverse_lazy('listar_posts')
