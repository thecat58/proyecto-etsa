from django.shortcuts import render




def home(request):
    return render(request, "index.html")
# Create your views here.


# librerias del crud
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

def Home(request):
    return render(request,"index.html")

class Listadomunicipio(ListView):
    model =  municipio

class municipioCrear(SuccessMessageMixin, CreateView):
    model =municipio
    form = municipio
    fields = "__all__"
    success_message ='municipio creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class municipioDetalle (DetailView):
    model =municipio

class  municipioActualizar(SuccessMessageMixin,UpdateView):
    model =  municipio
    form = municipio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'municipio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class municipioEliminar(SuccessMessageMixin, DeleteView): 
    model = municipio
    form = municipio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'municipio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
