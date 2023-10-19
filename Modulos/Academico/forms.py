from django import forms
from django.forms import DateInput, ModelForm, ClearableFileInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Modulos.Principal.models import *


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class MusiForm(forms.ModelForm):
	
	class Meta:
		model = Inv_Musica
		fields = '__all__'


class pedirMusica(forms.ModelForm):
	pedir = forms.IntegerField(min_value=1)

	class Meta:
		model = Pedir_Musica
		fields = ['material', 'pedir', 'Fecha_a_Pedir', 'Fecha_Limite']
		widgets = {
      		'Fecha_a_Pedir': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      		'Fecha_Limite': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    	}
		exclude = ['user']

#############################################################

class PintForm(forms.ModelForm):
	
	class Meta:
		model = Inv_Pintura
		fields = '__all__'

			
class pedirPintura(forms.ModelForm):
	pedir = forms.IntegerField(min_value=1)
	
	class Meta:
		model = Pedir_Pintura
		fields = ['material', 'pedir', 'Fecha_a_Pedir', 'Fecha_Limite']
		widgets = {
      		'Fecha_a_Pedir': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      		'Fecha_Limite': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    	}
		exclude = ['user']

#############################################################

class TAForm(forms.ModelForm):
	
	class Meta:
		model = Inv_TA
		fields = '__all__'


class pedirTA(forms.ModelForm):
	pedir = forms.IntegerField(min_value=1)
	
	class Meta:
		model = Pedir_TA
		fields = ['material', 'pedir', 'Fecha_a_Pedir', 'Fecha_Limite']
		widgets = {
      		'Fecha_a_Pedir': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      		'Fecha_Limite': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    	}
		exclude = ['user']

#############################################################

class DeportesForm(forms.ModelForm):
	
	class Meta:
		model = Inv_Deportes
		fields = '__all__'

			
class pedirDeportes(forms.ModelForm):
	pedir = forms.IntegerField(min_value=1)
	
	class Meta:
		model = Pedir_Deportes
		fields = ['material', 'pedir', 'Fecha_a_Pedir', 'Fecha_Limite']
		widgets = {
      		'Fecha_a_Pedir': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      		'Fecha_Limite': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    	}
		exclude = ['user']

#############################################################

class DanzasForm(forms.ModelForm):
	
	class Meta:
		model = Inv_Danzas
		fields = '__all__'


class pedirDanzas(forms.ModelForm):
	pedir = forms.IntegerField(min_value=1)

	class Meta:
		model = Pedir_Danzas
		fields = ['material', 'pedir', 'Fecha_a_Pedir', 'Fecha_Limite']
		widgets = {
      		'Fecha_a_Pedir': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      		'Fecha_Limite': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    	}
		exclude = ['user']

#############################################################

class FotoForm(forms.ModelForm):
	
	class Meta:
		model = Inv_Foto
		fields = '__all__'

class pedirFoto(forms.ModelForm):
	pedir = forms.IntegerField(min_value=1)
	
	class Meta:
		model = Pedir_Foto
		fields = ['material', 'pedir', 'Fecha_a_Pedir', 'Fecha_Limite']
		widgets = {
      		'Fecha_a_Pedir': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      		'Fecha_Limite': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    	}
		exclude = ['user']

#############################################################

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
		help_texts = {k:"" for k in fields }


class EditUsuarioForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username']

class EditUserForm(forms.ModelForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name']


class EditImageForm(forms.ModelForm):
	image = forms.ImageField()
	
	class Meta:
		model = Profile
		fields = ['image']
		widgets = {
            'image': CustomClearableFileInput
        }


class AñadirForm(forms.ModelForm):
	Numero_de_Documento_de_Identidad = forms.CharField(min_length=10, max_length=10)
	Celular = forms.CharField(min_length=10, max_length=10)
	Telefono = forms.CharField(min_length=7, max_length=7)
	
	class Meta:
		model = Profile
		fields = ['Tipo_de_Documento_de_Identidad', 'Numero_de_Documento_de_Identidad', 'Celular', 'Telefono']

#############################################################

class PostForm(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':8, 'cols':90, 'placeholder': '¿Qué está pasando?'}), required=True)
	image = forms.ImageField(required=False)

	class Meta:
		model = Post
		fields = ['content', 'image']
		widgets = {
            'image': CustomClearableFileInput
        }

#############################################################

class PostFormFoto(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':8, 'cols':90, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = PostFotografia
		fields = ['content']


#############################################################

class PostFormDanza(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':8, 'cols':90, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = PostDanzas
		fields = ['content']

#############################################################

class PostFormDepo(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':8, 'cols':90, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = PostDeportes
		fields = ['content']

#############################################################

class PostFormPint(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':8, 'cols':90, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = PostPintura
		fields = ['content']

#############################################################

class PostFormMusi(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':8, 'cols':90, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = PostMusica
		fields = ['content']

#############################################################

class PostFormTA(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':8, 'cols':90, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = PostTA
		fields = ['content']