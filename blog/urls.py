from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_posts, name='listar_posts'),
    path('post/<int:pk>/', views.detalhes_post, name='detalhes_post'),
    path('post/novo/', views.criar_post, name='criar_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/remover/', views.remover_post, name='remover_post'),
]