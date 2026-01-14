from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib import messages
from rest_framework import viewsets
from .serializers import BookSerializer

def dashboard(request):
    user_id = request.external_user_id
    username = request.external_username

    # Se não tiver token válido, não entra
    if not user_id:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=401)
    
    # Todos os contadores agora usam .filter(external_user_id=user_id)
    user_books = Book.objects.filter(external_user_id=user_id)
    
    books = user_books.order_by('-created_at')
    total_books = user_books.count()
    lidos = user_books.filter(status='lido').count()
    lendo = user_books.filter(status='lendo').count()
    quero_ler = user_books.filter(status='quero_ler').count()

    context = {
        'total_books': total_books,
        'lidos': lidos,
        'lendo': lendo,
        'quero_ler': quero_ler,
        'books': books,
        'username': username,
    }
    return render(request, 'bookshelf/dashboard.html', context)

def adicionar(request):
    if request.method == 'POST':
        # request.FILES é obrigatório para capturar a capa e o PDF
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.external_user_id = request.external_user_id
            book.save()

            messages.success(request, 'Livro adicionado com sucesso!')
            return redirect('dashboard')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form.html', {'form': form})

def editar(request, pk):
    # Busca o livro que pertence ao o usuário pelo ID (primary key) ou retorna 404 se não existir
    book = get_object_or_404(Book, pk=pk, external_user_id=request.external_user_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()

            messages.success(request, 'Alterações salvas com sucesso!')
            return redirect('dashboard')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookshelf/form.html', {'form': form, 'editing': True})

def excluir(request, pk):
    book = get_object_or_404(Book, pk=pk, external_user_id=request.external_user_id)
    if request.method == 'POST':
        book.delete()

        messages.success(request, 'O livro foi removido da sua estante.')
        return redirect('dashboard')
    
    # Se não for POST, mostra uma página de confirmação simples
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})

# NOVA API (JSON)
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        # A API só mostrará os livros do usuário dono do Token
        return Book.objects.filter(external_user_id=self.request.external_user_id)

    def perform_create(self, serializer):
        # Ao salvar via API, vincula automaticamente ao usuário do Token
        serializer.save(external_user_id=self.request.external_user_id)