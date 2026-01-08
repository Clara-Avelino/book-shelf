from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('ficcao', 'Ficção'), ('romance', 'Romance'), ('tecnico', 'Técnico'),
        ('fantasia', 'Fantasia'), ('suspense', 'Suspense'), ('biografia', 'Biografia'),
        ('historia', 'História'), ('ciencia', 'Ciência'), ('auto_ajuda', 'Auto-ajuda'),
        ('poesia', 'Poesia'), ('outros', 'Outros'),
    ]

    STATUS_CHOICES = [
        ('quero_ler', 'Quero Ler'),
        ('lendo', 'Lendo'),
        ('lido', 'Lido'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    published_year = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='quero_ler')
    
    # Uploads (Exigido pelo seu design do Figma)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    book_file = models.FileField(upload_to='ebooks/', null=True, blank=True)
    
    # Campo corrigido: apenas auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)
    external_user_id = models.IntegerField() 

    def __str__(self):
        return self.title