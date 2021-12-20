from django.urls import path
from AppPet import views

urlpatterns = [
  
    path('inicio', views.inicio, name="Inicio"),
    path('pajaros', views.pajaros, name ="Pajaros"),
    path('peces', views.peces, name="Peces"),
    path('perrosFormulario', views.perrosFormulario, name="PerrosFormulario"),

]
