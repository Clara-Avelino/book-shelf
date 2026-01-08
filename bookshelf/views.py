from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def dashboard(request):
    # Lógica para os contadores do topo da tela (Fiel ao seu print do Figma)
    total_books = Book.objects.count()
    lidos = Book.objects.filter(status='lido').count()
    lendo = Book.objects.filter(status='lendo').count()
    quero_ler = Book.objects.filter(status='quero_ler').count()

    # Pega todos os livros para listar abaixo
    books = Book.objects.all().order_by('-created_at')

    context = {
        'total_books': total_books,
        'lidos': lidos,
        'lendo': lendo,
        'quero_ler': quero_ler,
        'books': books,
        'username': 'Clara Maria', # Exemplo conforme seu Figma
    }

    return render(request, 'bookshelf/dashboard.html', context)

def adicionar(request):
    if request.method == 'POST':
        # request.FILES é obrigatório para capturar a capa e o PDF
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard') # Volta para a tela principal
    else:
        form = BookForm()
    return render(request, 'bookshelf/form.html', {'form': form})