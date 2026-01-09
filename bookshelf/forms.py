from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Descreve os campos que estarão no formulário
        fields = ['title', 'author', 'genre', 'published_year', 'status', 'cover_image', 'book_file', 'external_user_id']

        # Rótulos personalizados para os campos do formulário
        labels = {
            'title': 'Título do livro',
            'author': 'Autor',
            'genre': 'Gênero',
            'published_year': 'Ano de publicação',
            'status': 'Status de leitura',
            'cover_image': 'Imagem de capa',
            'book_file': 'Arquivo do livro (PDF)',
        }

        # Estilização e atributos dos campos do formulário
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-xl', 'placeholder': 'Título do Livro'}),
            'author': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-xl', 'placeholder': 'Nome do Autor'}),
            'genre': forms.Select(attrs={'class': 'w-full p-3 border rounded-xl'}),
            'status': forms.Select(attrs={'class': 'w-full p-3 border rounded-xl'}),
            'published_year': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-xl', 'placeholder': 'Ano de Publicação'}),
            'external_user_id': forms.HiddenInput(attrs={'value': 1}), # Temporário até integrar o JWT
        }