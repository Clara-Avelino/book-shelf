from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # O status_display mostra o nome amigável (ex: "Quero Ler" em vez de "quero_ler")
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'genre', 'published_year', 
            'status', 'status_display', 'cover_image', 'book_file', 
            'created_at', 'external_user_id'
        ]
        # O external_user_id deve ser apenas leitura para evitar que um 
        # usuário tente salvar livros no nome de outro via API.
        read_only_fields = ['external_user_id'] # Impede que mudem o dono via API