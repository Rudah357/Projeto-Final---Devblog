from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Categoria
from .forms import ContatoForm, ComentarioForm
from .serializers import ArtigoSerializer, CategoriaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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


def fale_conosco(request):
    if request.method == 'POST':
        formulario = ContatoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')
        
    else:
        formulario = ContatoForm()

    contexto = {
        'form': formulario
    }

    return render(request, 'blog/contato.html', contexto)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_criar_artigos(request):
    serializer = ArtigoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def api_listar_artigos(request):

    artigos = Artigo.objects.all()
    serializer = ArtigoSerializer(artigos, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def api_listar_categorias(request):

    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)

    return Response(serializer.data)


def detalhe_noticia(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.save()
            return redirect('detalhe_noticia', pk=artigo.pk)
    else:
        form = ComentarioForm()

    return render(request, 'blog/detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form
    })
