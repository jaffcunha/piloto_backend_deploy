from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader, Context
from sistema.forms import *
from sistema.models import *
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib import auth
from django.conf import settings
import os
from os import path
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# Cadastrar, editar e excluir pessoas
# def cadastrar_membro(request):
# 	if request.method == 'GET':
# 		pessoa_form = PessoaForm()
# 	if request.method == 'POST':
# 		pessoa_form = PessoaForm(request.POST)
# 		if pessoa_form.is_valid():
# 			pessoa_form.save()
# 			sucesso = True
# 			return HttpResponseRedirect('/cadastrar_membro/')
# 		else:
# 			dados_incorretos = True
# 			return render(request, 'cadastrar_membro.html', locals())
# 	return render(request, 'cadastrar_membro.html', locals())

# def editar_membro(request, id_pessoa):
# 	objeto = Pessoa.objects.get(id = id_pessoa)
# 	if request.method == 'GET':
# 		pessoa_form = PessoaForm(instance = objeto)
# 	if request.method == 'POST':
# 		pessoa_form = PessoaForm(request.POST,instance = objeto)
# 		if pessoa_form.is_valid():
# 			pessoa_form.save()
# 			sucesso = True
# 			return HttpResponseRedirect('/editar_membro/%s' %id_pessoa)
# 		else:
# 			dados_incorretos = True
# 			return render(request, 'editar_membro.html', locals())
# 	return render(request, 'editar_membro.html', locals())

# def visualizar_membros(request):
#     pessoas = Pessoa.objects.all()
#     return render(request, 'visualizar_membros.html', locals())

# def excluir_membro(request, id_pessoa):
# 	objeto = Pessoa.objects.get(id = id_pessoa)
# 	objeto.delete()
# 	messages.success(request, 'O cadastro foi deletado')
# 	return HttpResponseRedirect('/visualizar_membros/')

# def home(request):
# 	return render(request, 'home.html', locals())

# def login(request):
# 	login_incorreto = False
# 	if request.method == 'POST':
# 		usuario = request.POST.get("username")
# 		senha = request.POST.get("password")
# 		user = authenticate(username=usuario, password=senha)
# 		if user is not None:
# 			auth.login(request, user)
# 			return HttpResponseRedirect('/home/')
# 		else:
# 			login_incorreto = True
# 			return render(request, 'login.html', locals())
# 	else:
# 		return render(request, 'login.html', locals())

# def logout(request):
# 	auth.logout(request)
# 	return HttpResponseRedirect('/login/')

# Inicio da implementacao/teste do Custom Lookup

def implementacao_lookup_exact(request):

	# Irei testar o filtro quando procuro uma palavra
	# exatamente como ela esta escrita, utilizando o __exact.

    pessoas = Pessoa.objects.filter(cargo__exact = "docente")
    return render(request, 'visualizar_membros.html', locals())

def implementacao_lookup_iexact(request):

    # Irei testar o filtro quando procuro uma palavra
    # mas que nao necessariamente estao todas iguaisl, utilizando o __iexact.

    pessoas = Pessoa.objects.filter(cargo__iexact = "docente")
    return render(request, 'visualizar_membros.html', locals())

def implementacao_custom_lookup(request):

	# Irei testar o filtro com um custom lookup
	# Leia atentamente os passos para se utilizar o custom lookup na documentacao
	# Primeiramente na models implementa-se o codigo
	# Depois avisamos o Django sobre ele

	pessoas = Pessoa.objects.filter(idade__func = "17")
	return render(request, 'visualizar_membros.html', locals())

# Inicio da implementacao/teste da Transformacao

def implementacao_transformacao(request):

	# Irei testar o filtro com uma transformacao que ira me dar
	# todos os membros cadastrados com idade < 18 anos.

	pessoas = Pessoa.objects.filter(idade__idmenor__lt = "18")
	return render(request, 'visualizar_membros.html', locals())
