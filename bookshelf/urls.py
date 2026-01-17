from django.urls import path, include
from . import views
from drf_spectacular.views import  SpectacularAPIView, SpectacularSwaggerView # Gera o JSON da API e mostra o Swagger UI
from rest_framework.routers import DefaultRouter # Roteador para ViewSets

# inicializa as rotas da API
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book-api')

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('adicionar/', views.adicionar, name='adicionar'), 
    path('editar/<int:pk>/', views.editar, name='editar'), 

    path('excluir/<int:pk>/', views.excluir, name='excluir'),
    
    # Swagger e OpenAPI (http://127.0.0.1:8000/api/schema/swagger-ui/)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # JSON técnico da API
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Página visual
    
    # Rota para a API (http://127.0.0.1:8000/api/books/)
    path('api/', include(router.urls)),
]

