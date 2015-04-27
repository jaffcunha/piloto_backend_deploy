from django.forms import ModelForm, TextInput, Select, PasswordInput, Textarea, CharField
from django import forms
from sistema.models import *
from django.contrib.auth.forms import PasswordChangeForm

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = ('nome_pessoa', 'idade', 'genero', 'cpf', 'empresa', 'cargo')