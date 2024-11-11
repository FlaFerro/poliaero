from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()  # Obtém o post atual
        # Ordena os comentários do mais recente para o mais antigo
        context['comments'] = post.comments.all().order_by('-created_date')
        return context

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

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            comment = Comment(post=post, author=request.user, text=text, created_date=timezone.now())
            comment.save()
        return redirect('detalhes_post', pk=post.pk)