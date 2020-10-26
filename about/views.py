from django.shortcuts import render

# Create your views here.

def get_presidente_info(request):
    return render(request, "about/presidente.html")

def get_vice_info(request):
	return render(request, "about/vice.html")