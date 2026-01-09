from django.urls import path
from . import views
from drf_spectacular.views import  SpectacularAPIView, SpectacularSwaggerView # Gera o JSON da API e mostra o Swagger UI

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('adicionar/', views.adicionar, name='adicionar'), 
    path('editar/<int:pk>/', views.editar, name='editar'), 
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # JSON técnico da API
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Página visual
]