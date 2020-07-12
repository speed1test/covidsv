from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User
from django.core import mail

from apps.covid.models import *

def login(request):

	if(request.method == 'POST'):

		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.error(request,'Credenciales inválidas')
			return redirect('/')

	else:
		return render(request,'users/login.html')
def logout(request):
	auth.logout(request)
	return redirect('/')

def gestion_laboratorista(request):	
	laboratoristas = Laboratorista.objects.all()
	contexto = {'laboratoristas': laboratoristas,}
	return render(request, 'gestion_usuarios/gestion_laboratorista.html', contexto)

def eliminar_laboratorista(request):

	Laboratorista.objects.filter(id=request.POST['id_delete']).delete()
	User.objects.filter(pk=request.POST['user_delete']).delete()

	return redirect('laboratorista')


# Create your views here.
