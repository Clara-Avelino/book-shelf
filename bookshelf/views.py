from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth import logout
import requests
import json

from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated


def dashboard(request):
    user_id = request.external_user_id
    username = request.external_username

    # Se não tiver token válido, retorna para o login
    if not user_id:
       return redirect('login')
    
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
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # A API só mostrará os livros do usuário dono do Token
        return Book.objects.filter(external_user_id=self.request.external_user_id)

    def perform_create(self, serializer):
        # Ao salvar via API, vincula automaticamente ao usuário do Token
        serializer.save(external_user_id=self.request.external_user_id)

# def login_view(request):
#     return render(request, 'bookshelf/login.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        body = {
            "email": email,
            "password": password
        }

        try:
            # Chamada para a API
            response = requests.post(
                'https://usuarioapi-production.up.railway.app/api/login/', 
                data=json.dumps(body), 
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 200:
                data = response.json()
                
                # Guardamos o token na SESSÃO do Django
                request.session['auth_token'] = data.get('access') 
                request.session['user_email'] = email
                request.session.modified = True  # Força o Django a salvar a sessão
                messages.success(request, "Login realizado com sucesso!")
                return redirect('dashboard')
            else:
                messages.error(request, "E-mail ou senha inválidos.")
        
        except Exception:
            messages.error(request, "Erro ao conectar com o serviço de autenticação.")

    return render(request, 'bookshelf/login.html')


def register_view(request):
    return render(request, 'bookshelf/register.html')

def register_user(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        body = {
            "username": username,
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name
        }
        response = requests.post('https://usuarioapi-production.up.railway.app/api/registro/', data=json.dumps(body), headers={'Content-Type': 'application/json'})
        if response.status_code == 201:
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')