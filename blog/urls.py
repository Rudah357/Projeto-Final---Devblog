from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sobre/', views.sobre_nos, name="sobre_nos"),
    path('noticia/<int:id>/', views.detalhe_noticia, name='detalhe_noticia')
]