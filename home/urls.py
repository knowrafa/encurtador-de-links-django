from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home),
    path('encurtador/', views.encurtador),
    path('tabela/', views.mostrar_tabela)
]