from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Exibe estas colunas na lista de livros
    list_display = ('title', 'author', 'genre', 'status', 'published_year')
    
    # Adiciona filtros laterais baseados no seu Figma
    list_filter = ('status', 'genre')
    
    # Permite buscar por título ou autor
    search_fields = ('title', 'author')