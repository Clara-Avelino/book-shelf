# 📚 Book Shelf - Sistema de Gerenciamento de Acervos

O **Book Shelf** é uma aplicação Full Stack desenvolvida em **Django** para o gerenciamento de livros e e-books. O projeto utiliza uma arquitetura baseada em microsserviços e separação de responsabilidades em diferentes plataformas (PaaS).

## 🚀 Arquitetura do Projeto (Multi-PaaS)

Para cumprir as exigências de escalabilidade e nuvem, o projeto está dividido em:

- **PaaS 01 (Front-end):** Integrado via Django Templates com estilização **Tailwind CSS**.
- **PaaS 02 (Back-end):** **Django 5.x** e **Django Rest Framework** (Processamento e lógica).
- **PaaS 03 (Banco de Dados):** **PostgreSQL** hospedado no **Neon.tech**.

---

## 🛠️ Instalação e Configuração

Siga os passos abaixo para replicar o ambiente de desenvolvimento.

### 1. Clonagem e Ambiente Virtual

No terminal, execute:

```bash
# Clone o repositório
git clone https://github.com/Clara-Avelino/book-shelf.git

# Acesse o diretório do projeto
cd book-shelf

# Criação do ambiente virtual
python -m venv venv

# Ativação do ambiente no Windows:
venv\Scripts\activate

# Ativação do ambiente no Linux/Mac:
source venv/bin/activate
```

### 2. Instalação de Dependências

Instale cada pacote necessário para o funcionamento do sistema:

```bash
pip install django djangorestframework django-cors-headers python-dotenv dj-database-url psycopg2-binary drf-spectacular Pillow

```

### 3. Configuração das Variáveis de Ambiente (`.env`)

Primeiro, siga os passos para criar banco de dados no `Neon`

- Acesse o site oficial [Neon](https://console.neon.tech/)
- Clica em `Projetos`, `Novo projeto`
- Ira abrir um modal para criar e configurar
- Dê um nome para o projeto `BookShelf-DB`
- Escolha a versão `17` do `Postgres`
- Escolha provedor de serviços em nuvem `AWS`
- A região `AWS América do Sul Leste 1 (São Paulo)`
- E clique em `Criar`

![alt text](./bookshelf/templates/img/image-1.png)

Agora para conectar ao banco de dados, clique em `Conectar`.

![alt text](./bookshelf/templates/img/image-2.png)

Ira abrir outro modal, copie a `String de conexão`

![alt text](./bookshelf/templates/img/image-3.png)

Crie um arquivo chamado `.env` na raiz do projeto e cole a `String de conexão` na variável `DB_URL` conforme o exemplo abaixo:

```env
DEBUG=True
SECRET_KEY=sua_chave_secreta_aqui
DB_URL=postgresql://USUARIO:SENHA@HOST/neondb?sslmode=require
```

---

## 🏗️ Execução e Migrações

Com o banco de dados conectado, é necessário criar as tabelas e iniciar o servidor.

### 1. Sincronização com o Banco Neon

```bash
# Detectar mudanças nos modelos
python manage.py makemigrations

# Aplicar as tabelas no Neon (PostgreSQL)
python manage.py migrate

```

### 2. Criação de Administrador

Para testar o CRUD via painel administrativo:

```bash
python manage.py createsuperuser
```

Defina um nome de usuário, e-mail e senha quando solicitado.

- Acesse: [http://127.0.0.1:8000/admin](https://www.google.com/search?q=http://127.0.0.1:8000/admin)
- Faça login com as credenciais criadas.
- Procure a tabela `Bookshelf` para gerenciar livros e e-books.
- Cadastre um livro para visualizar no dashboard, se funcionar, está tudo certo no django admin!

### 3. Iniciar o Servidor

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000 e cadastre um novo livro em para visualizar no dashboard.

![alt text](./bookshelf/templates/img/image-4.png)

Em http://127.0.0.1:8000/adicionar/ você pode adicionar novos livros via formulário.

![alt text](./bookshelf/templates/img/image-5.png)

### 4. Visualização das tabelas no Neon

Acesse o painel do Neon e em `Branch`, vá em `Tables`, selecione a tabela `bookshelf_book` para visualizar os dados cadastrados via `Django Admin` ou formulário.
![alt text](./bookshelf/templates/img/image-6.png)

> Seu projeto Book Shelf está pronto para uso!

**Dica de Manutenção:** Caso precise atualizar o banco de dados, sempre verifique a conexão no Neon via `SQL Editor` antes de rodar o `migrate`.

---

## 📁 Estrutura de Arquivos

```text
/book-shelf
├── bookshelf/                    # App principal do Book Shelf
│   ├── static/                   # Arquivos de estilo e scripts
│   ├── templates/                # Telas HTML (Dashboard e Formulários)
│   |   ├── bookshelf/            # Templates específicos do app
│   |   |    ├── dashboard.html   # Tela principal do dashboard
│   |   |    └── form.html        # Formulário de cadastro
│   |   └── base.html             # Template base
│   ├── admin.py                  # Configuração do Painel Administrativo
│   ├── forms.py                  # Validação de entradas e uploads
│   ├── models.py                 # Modelagem do Banco de Dados
│   ├── urls.py                   # Rotas do aplicativo
│   └── views.py                  # Lógica de negócio e contadores
├── core/                         # Configurações globais do Django
│   ├── settings.py               # Configurações do projeto
│   ├── urls.py                   # Rotas principais do projeto
├── media/                        # Armazenamento de capas e arquivos
│   ├── covers/                   # Capas dos livros
│   └── ebooks/                   # Arquivos dos e-books
├── venv/                         # Ambiente virtual Python
├── .env                          # Credenciais sensíveis (PaaS 03)
├── .gitignore                    # Arquivos e pastas ignoradas pelo Git
├── manage.py                     # CLI do Django
├── README.md                     # Documentação do projeto
└── requirements.txt              # Lista de dependências
```

### 🛠️ Tecnologias usadas

**Front-end**

- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

**Back-end**

- ![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- ![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)

**Banco de Dados**

- ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
- ![Neon](https://img.shields.io/badge/Neon-2DFFEC?style=for-the-badge&logo=neon&logoColor=white)

---

### Colaboradores

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; align-items: start;">
  <!-- Dev 1 -->
  <div style="text-align: center;">
    <img src="https://github.com/Clara-Avelino.png" alt="Clara Avelino" style="width: 140px; height: 140px; object-fit: cover; border-radius: 50%;">
    <div style="margin-top: 0.75rem; font-weight: bold;">Clara Avelino</div>
    <a href="https://github.com/Clara-Avelino" target="_blank" rel="noopener">Clara-Avelino</a>
  </div>
  <!-- Dev 2 -->
  <div style="text-align: center;">
    <img src="https://github.com/Clara-Avelino.png" alt="Clara Avelino" style="width: 140px; height: 140px; object-fit: cover; border-radius: 50%;">
    <div style="margin-top: 0.75rem; font-weight: bold;">Clara Avelino</div>
    <a href="https://github.com/Clara-Avelino" target="_blank" rel="noopener">Clara-Avelino</a>
  </div>
  <!-- Dev 3 -->
  <div style="text-align: center;">
    <img src="https://github.com/Clara-Avelino.png" alt="Clara Avelino" style="width: 140px; height: 140px; object-fit: cover; border-radius: 50%;">
    <div style="margin-top: 0.75rem; font-weight: bold;">Clara Avelino</div>
    <a href="https://github.com/Clara-Avelino" target="_blank" rel="noopener">Clara-Avelino</a>
  </div>

</div>

---

<div style="text-align: center;">Feito com ❤️ por Clara Avelino.</div>
