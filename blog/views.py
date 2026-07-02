from django.shortcuts import render, get_object_or_404
from .models import Artigo, Categoria

def detalhe_noticia(request, id):
    
    noticia = get_object_or_404(Artigo, id=id)
    lista_categorias = Categoria.objects.all()
    
    context = {
        'noticia': noticia,
        'lista_categorias': lista_categorias,
    }
    return render(request, 'blog/detalhe.html', context)

def home(request):
    categoria_id = request.GET.get('categoria')

    noticias = Artigo.objects.all().order_by('-data_publicacao')
    categorias = Categoria.objects.all()

    if categoria_id:
            noticias = noticias.filter(categoria_id=categoria_id)

    lista_categorias = Categoria.objects.all()

    contexto = {
        'lista_artigos': noticias,
        'lista_categorias': categorias
    }
    
    return render(request, 'blog/index.html', contexto)

def sobre_nos(request):

    return render(request, 'blog/sobre.html')
