from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib import messages

def dashboard(request):
    user_id = request.external_user_id
    username = request.external_username

    # Se não tiver token válido, não entra
    if not user_id:
        return JsonResponse(
            {'error': 'Usuário não autenticado'},
            status=401
        )
    
    # Isolamento de dados (filtrado por usuário)
    books = Book.objects.filter(external_user_id=user_id).order_by('-created_at')
    
    total_books = Book.objects.count()
    lidos = Book.objects.filter(status='lido').count()
    lendo = Book.objects.filter(status='lendo').count()
    quero_ler = Book.objects.filter(status='quero_ler').count()

    

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
            form.save()

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