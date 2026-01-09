from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('adicionar/', views.adicionar, name='adicionar'), 
    path('editar/<int:pk>/', views.editar, name='editar'), 
    path('excluir/<int:pk>/', views.excluir, name='excluir'), 
]