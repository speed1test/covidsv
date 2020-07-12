from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import date, datetime
from apps.covid.models import *

def index(request):
	return render(request, 'index.html')
def gestion_clientes(request):	
	clientes = Laboratoristas.objects.all()
	contexto = {'clientes': clientes,}
	return render(request, 'gestion_usuarios/gestion_laboratoristas.html', contexto)
# Create your views here.
