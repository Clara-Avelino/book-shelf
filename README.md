# 📚 Book Shelf - Sistema de Gerenciamento de Acervos

O **Book Shelf** é uma aplicação Full Stack desenvolvida em **Django** para o gerenciamento de livros e e-books. O projeto utiliza uma arquitetura baseada em microsserviços e separação de responsabilidades em diferentes plataformas (PaaS).

## 🚀 Arquitetura do Projeto (Multi-PaaS)

Para cumprir as exigências de escalabilidade e nuvem, o projeto está dividido em:

- **PaaS 01 (Front-end):** Integrado via Django Templates com estilização **Tailwind CSS** (Cores: `#fbfae6`, `#93b90e`, `#e3b91c`).
- **PaaS 02 (Back-end):** **Django 5.x** e **Django Rest Framework** (Processamento e lógica).
- **PaaS 03 (Banco de Dados):** **PostgreSQL** hospedado no **Neon.tech**.

---

## 🛠️ Instalação e Configuração

Siga os passos abaixo para replicar o ambiente de desenvolvimento.

### 1. Clonagem e Ambiente Virtual

No terminal, execute:

```bash
# Clone o repositório ou crie a pasta
mkdir bookshelf-project && cd bookshelf-project

# Criação do ambiente virtual
python -m venv venv

# Ativação do ambiente
# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate

```

### 2. Instalação de Dependências

Instale cada pacote necessário para o funcionamento do sistema:

```bash
pip install django djangorestframework django-cors-headers python-dotenv dj-database-url psycopg2-binary drf-spectacular Pillow

```

### 3. Configuração das Variáveis de Ambiente (`.env`)

Crie um arquivo chamado `.env` na raiz do projeto e adicione suas credenciais do **Neon (PaaS 03)**:

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

### 3. Iniciar o Servidor

```bash
python manage.py runserver

```

Acesse: [http://127.0.0.1:8000](https://www.google.com/search?q=http://127.0.0.1:8000)

---

## 📁 Estrutura de Arquivos

```text
/bookshelf-project
├── core/                 # Configurações globais do Django
├── bookshelf/            # App principal do Book Shelf
│   ├── static/           # Arquivos de estilo e scripts
│   ├── templates/        # Telas HTML (Dashboard e Formulários)
│   ├── admin.py          # Configuração do Painel Administrativo
│   ├── forms.py          # Validação de entradas e uploads
│   ├── models.py         # Modelagem do Banco de Dados
│   └── views.py          # Lógica de negócio e contadores
├── media/                # Armazenamento de capas (covers) e arquivos (ebooks)
├── .env                  # Credenciais sensíveis (PaaS 03)
├── manage.py             # CLI do Django
└── requirements.txt      # Lista de dependências

```

---

**Dica de Manutenção:** Caso precise atualizar o banco de dados, sempre verifique a conexão no Neon via SQL Editor antes de rodar o `migrate`.
