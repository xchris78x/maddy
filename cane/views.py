from django.shortcuts import render
from .models import Foto, Blog, HomePage

def foto(request):
    fotos = Foto.objects.all()
    return render(request, 'cane/foto.html', {'fotos': fotos})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'cane/blog.html', {'blogs': blogs})


def home(request):
    return render(request, 'cane/index.html')

def contatti(request):
    return render(request, 'cane/contatti.html')


def home_page_view(request):
    home_page = HomePage.objects.first()
    return render(request, 'index.html', {'home_page': home_page})



