from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")

def encurtador(request):
    return render(request, "encurtador/encurtador.html")

def mostrar_tabela(request):
	return render(request, "column/index.html")