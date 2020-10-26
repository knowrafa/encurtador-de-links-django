from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('presidente/', views.get_presidente_info),
    path('vice/', views.get_vice_info)
]