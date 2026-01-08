from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_year', 'status', 'cover_image', 'book_file', 'external_user_id']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-xl', 'placeholder': 'Título do Livro'}),
            'author': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-xl', 'placeholder': 'Nome do Autor'}),
            'genre': forms.Select(attrs={'class': 'w-full p-3 border rounded-xl'}),
            'status': forms.Select(attrs={'class': 'w-full p-3 border rounded-xl'}),
            'published_year': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-xl'}),
            'external_user_id': forms.HiddenInput(attrs={'value': 1}), # Temporário até integrar o JWT
        }