from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('adicionar/', views.adicionar, name='adicionar'), 
    path('editar/<int:pk>/', views.editar, name='editar'), 
    path('excluir/<int:pk>/', views.excluir, name='excluir'), 
    
]