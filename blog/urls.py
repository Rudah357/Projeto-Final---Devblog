from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sobre/', views.sobre_nos, name="sobre_nos"),
    path('noticia/<int:id>/', views.detalhe_noticia, name='detalhe_noticia'),
    path('contato/', views.fale_conosco, name="fale_conosco"),
    path('api/artigos/', views.api_listar_artigos, name="api_artigos"),
    path('api/categorias/', views.api_listar_categorias, name="api_categorias"),
    path('api/artigos/novo/', views.api_criar_artigos, name="api_criar_artigo")
]