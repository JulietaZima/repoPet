from django.shortcuts import render

from django.http import HttpResponse

from AppPet.models import *

# Create your views here.

def inicio(request):

    return render(request, 'AppPet/inicio.html')

def pajaros(request):

    if request.method == "POST":
        
        perroInsta = Pajaro(especie = request.POST["especie"], zona = request.POST["zona"], esExotico = request.POST["esExotico"])

        perroInsta.save()

        return render(request, 'AppPet/inicio.html')
   
    return render(request, 'AppPet/pajaros.html')

def peces(request):

    if request.method == "POST":
        
        pezInsta = Pez(especie = request.POST["especie"], deAguaSalada = request.POST["deAguaSalada"])

        pezInsta.save()

        return render(request, 'AppPet/inicio.html')
   
    return render(request, 'AppPet/peces.html')

def perrosFormulario(request):

    if request.method == "POST":
        
        perroInsta = Perro(raza = request.POST["raza"], edad = request.POST["edad"], esCastrado = request.POST["esCastrado"])

        perroInsta.save()

        return render(request, 'AppPet/inicio.html')
   
    return render(request, 'AppPet/perrosFormulario.html')