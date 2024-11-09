from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.urls import reverse

def listar_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/listar_posts.html', {'posts': posts})

def detalhes_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalhes_post.html', {'post': post})

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo post no banco de dados
            return redirect('listar_posts')  # Redireciona para a lista de posts
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form})

def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # Salva as alterações no post existente
            return redirect('detalhes_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/form_post.html', {'form': form})
