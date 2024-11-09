from django.urls import path
from .views import ListarPostsView, DetalhesPostView, CriarPostView, EditarPostView, DeletarPostView

urlpatterns = [
    path('', ListarPostsView.as_view(), name='listar_posts'),
    path('post/<int:pk>/', DetalhesPostView.as_view(), name='detalhes_post'),
    path('post/novo/', CriarPostView.as_view(), name='criar_post'),
    path('post/<int:pk>/editar/', EditarPostView.as_view(), name='editar_post'),
    path('post/<int:pk>/deletar/', DeletarPostView.as_view(), name='deletar_post'),
]
