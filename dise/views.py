# diseño/views.py
from django.shortcuts import render

def mostrar(request):
    return render(request, 'mostrar.html')