from django import forms
from .models import MensagemContato, Comentario

class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato

        fields = ['nome', 'email', 'mensagem']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'texto']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Digite seu nome...'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Escreva seu comentário aqui...'
            }),
        }
    