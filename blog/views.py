from django.shortcuts import render, get_object_or_404
from .models import Artigo, Categoria

def lista_artigos(request):
    lista_artigos = Artigo.objects.all()
    categoria_selecionada = None

    categoria_slug = request.GET.get('categoria')

    if categoria_slug:
        categoria_selecionada = get_object_or_404(Categoria, slug=categoria_slug)
        lista_artigos = lista_artigos.filter(categoria=categoria_selecionada)

    context = {
        'lista_artigos': lista_artigos,
        'categoria_atual': categoria_selecionada,
    }
    return render(request, 'blog/seu_template.html', context)

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
    categoria_selecionada = None

    if categoria_id:
        categoria_selecionada = get_object_or_404(Categoria, id=categoria_id)
        noticias = noticias.filter(categoria_id=categoria_id)

    contexto = {
        'lista_artigos': noticias,
        'lista_categorias': categorias,
        'categoria_atual': categoria_selecionada,
    }
    
    return render(request, 'blog/index.html', contexto)

def sobre_nos(request):

    return render(request, 'blog/sobre.html')
