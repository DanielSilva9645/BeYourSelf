from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .forms import *
from .models import *
from Modulos.Principal.filters import *
from Modulos.Principal.models import Event
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

##########################-Posts-#########################	

@login_required
def Postss(request):

	posts = Post.objects.all()
	myfilter = PostFilter(request.GET, queryset=posts)
	posts = myfilter.qs

	context = { 'posts': posts, 'myfilter': myfilter }
	return render(request, 'Post.html', context)

@login_required
def CrearPost(request): 			
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form			
			Cont = post.cleaned_data['content']
			archivo = request.FILES.get('image')		
			#archivo = post.cleaned_data['image']
			post.user = current_user
			post.content = Cont
			post.image = archivo
			post.save()
			messages.success(request, 'Post enviado')
			return redirect(to='Post')
	else:
		form = PostForm()
	return render(request, 'NewPosts.html', {'form' : form })
        


@login_required
def modificar_Post(request, codigo):
	carrera = get_object_or_404(Post, codigo=codigo)#busca un elemento

	data={ 'form' : PostForm(instance=carrera)}

	if request.method=='POST':
		formulario=PostForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Post Modificado Correctamente")
			return redirect(to='Post')
		data["form"]=formulario	
	return render(request, 'modificar_Post.html', data)

@login_required
def eliminar_Post(request, codigo):
	carrera = get_object_or_404(Post, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Eliminado Correctamente")
	return redirect(to="Post")

#########################-Posts Fotografia-#########################	

@login_required
def PostFotografias(request):

	posts = PostFotografia.objects.all()
	myfilter = PostFotoFilter(request.GET, queryset=posts)
	posts = myfilter.qs

	context = { 'postsFoto': posts, 'myfilter': myfilter }
	return render(request, 'PostFotografia.html', context)

@login_required
def CrearPostFoto(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostFormFoto(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Comentario Publicado Correctamente')
			return redirect(to='PostFotografia')
	else:
		form = PostFormFoto()
	return render(request, 'NewPostsFotos.html', {'form' : form })

@login_required
def modificar_PostFoto(request, codigo):
	carrera = get_object_or_404(PostFotografia, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormFoto(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormFoto(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			return redirect(to='PostFotografia')
		data["form"]=formulario	
	return render(request, 'modificar_PostFoto.html', data)

@login_required
def modificar_PostFoto2(request, codigo):
	carrera = get_object_or_404(PostFotografia, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormFoto(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormFoto(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			usern = carrera.user
			return redirect('PostsPedidos', username=usern)
		data["form"]=formulario	
	return render(request, 'modificar_PostFoto2.html', data)

@login_required
def eliminar_PostFoto(request, codigo):
	carrera = get_object_or_404(PostFotografia, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	return redirect(to="PostFotografia")

@login_required
def eliminar_PostFoto2(request, codigo):
	carrera = get_object_or_404(PostFotografia, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

#########################-Posts Danzas-#########################

@login_required
def PostDanzass(request):

	posts = PostDanzas.objects.all()
	time = "hace 6 días,11 horas"
	myfilter = PostDanzasFilter(request.GET, queryset=posts)
	posts = myfilter.qs

	context = { 'postsDanzas': posts, 'myfilter': myfilter, 'time':time }
	return render(request, 'PostDanzas.html', context)

@login_required
def CrearPostDanza(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostFormDanza(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Comentario Publicado Correctamente')
			return redirect(to='PostDanzass')
	else:
		form = PostFormDanza()
	return render(request, 'NewPostsDanza.html', {'form' : form })

@login_required
def modificar_PostDanzass(request, codigo):
	carrera = get_object_or_404(PostDanzas, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormDanza(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormDanza(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			return redirect(to='PostDanzass')
		data["form"]=formulario	
	return render(request, 'modificar_PostDanzass.html', data)

@login_required
def modificar_PostDanzass2(request, codigo):
	carrera = get_object_or_404(PostDanzas, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormDanza(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormDanza(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			usern = carrera.user
			return redirect('PostsPedidos', username=usern)
		data["form"]=formulario	
	return render(request, 'modificar_PostDanzass2.html', data)

@login_required
def eliminar_PostDanzass(request, codigo):
	carrera = get_object_or_404(PostDanzas, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	return redirect(to="PostDanzass")

@login_required
def eliminar_PostDanzass2(request, codigo):
	carrera = get_object_or_404(PostDanzas, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

#########################-Posts Deportes-#########################

@login_required
def PostDeportess(request):

	posts = PostDeportes.objects.all()
	myfilter = PostDepoFilter(request.GET, queryset=posts)
	posts = myfilter.qs

	context = { 'postsdeportes': posts, 'myfilter': myfilter }
	return render(request, 'PostDeportes.html', context)

@login_required
def CrearPostDepo(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostFormDepo(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Comentario Publicado Correctamente')
			return redirect(to='PostDeportess')
	else:
		form = PostFormDepo()
	return render(request, 'NewPostsDepo.html', {'form' : form })

@login_required
def modificar_PostDeportess(request, codigo):
	carrera = get_object_or_404(PostDeportes, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormDepo(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormDepo(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			return redirect(to='PostDeportess')
		data["form"]=formulario	
	return render(request, 'modificar_PostDeportess.html', data)

@login_required
def modificar_PostDeportess2(request, codigo):
	carrera = get_object_or_404(PostDeportes, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormDepo(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormDepo(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			usern = carrera.user
			return redirect('PostsPedidos', username=usern)
		data["form"]=formulario	
	return render(request, 'modificar_PostDeportess2.html', data)

@login_required
def eliminar_PostDeportess(request, codigo):
	carrera = get_object_or_404(PostDeportes, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	return redirect(to="PostDeportess")

@login_required
def eliminar_PostDeportess2(request, codigo):
	carrera = get_object_or_404(PostDeportes, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

#########################-Posts Pintura-#########################

@login_required
def PostPinturass(request):

	posts = PostPintura.objects.all()
	myfilter = PostPintFilter(request.GET, queryset=posts)
	posts = myfilter.qs

	context = { 'postspinturass': posts, 'myfilter': myfilter }
	return render(request, 'PostPintura.html', context)

@login_required
def CrearPostPint(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostFormPint(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Comentario Publicado Correctamente')
			return redirect(to='PostPinturass')
	else:
		form = PostFormPint()
	return render(request, 'NewPostsPint.html', {'form' : form })

@login_required
def modificar_PostPint(request, codigo):
	carrera = get_object_or_404(PostPintura, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormPint(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormPint(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			return redirect(to='PostPinturass')
		data["form"]=formulario	
	return render(request, 'modificar_PostPint.html', data)

@login_required
def modificar_PostPint2(request, codigo):
	carrera = get_object_or_404(PostPintura, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormPint(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormPint(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			usern = carrera.user
			return redirect('PostsPedidos', username=usern)
		data["form"]=formulario	
	return render(request, 'modificar_PostPint2.html', data)

@login_required
def eliminar_PostPint(request, codigo):
	carrera = get_object_or_404(PostPintura, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	return redirect(to="PostPinturass")

@login_required
def eliminar_PostPint2(request, codigo):
	carrera = get_object_or_404(PostPintura, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

#########################-Posts Musica-#########################

@login_required
def PostMusicass(request):

	posts = PostMusica.objects.all()
	myfilter = PostMusiFilter(request.GET, queryset=posts)
	posts = myfilter.qs

	context = { 'postsmusik': posts, 'myfilter': myfilter }
	return render(request, 'PostMusica.html', context)

@login_required
def CrearPostMusi(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostFormMusi(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Comentario Publicado Correctamente')
			return redirect(to='PostMusicass')
	else:
		form = PostFormMusi()
	return render(request, 'NewPostsMusi.html', {'form' : form })

@login_required
def modificar_PostMusi(request, codigo):
	carrera = get_object_or_404(PostMusica, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormMusi(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormMusi(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			return redirect(to='PostMusicass')
		data["form"]=formulario	
	return render(request, 'modificar_PostMusi.html', data)

@login_required
def modificar_PostMusi2(request, codigo):
	carrera = get_object_or_404(PostMusica, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormMusi(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormMusi(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			usern = carrera.user
			return redirect('PostsPedidos', username=usern)
		data["form"]=formulario	
	return render(request, 'modificar_PostMusi2.html', data)

@login_required
def eliminar_PostMusi(request, codigo):
	carrera = get_object_or_404(PostMusica, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	return redirect(to="PostMusicass")

@login_required
def eliminar_PostMusi2(request, codigo):
	carrera = get_object_or_404(PostMusica, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

#########################-Posts Expresion Corporal-#########################

@login_required
def PostTAss(request):

	posts = PostTA.objects.all()
	myfilter = PostTAFilter(request.GET, queryset=posts)
	posts = myfilter.qs

	context = { 'postsTAS': posts, 'myfilter': myfilter }
	return render(request, 'PostTA.html', context)

@login_required
def CrearPostTA(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostFormTA(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Comentario Publicado Correctamente')
			return redirect(to='PostTAss')
	else:
		form = PostFormTA()
	return render(request, 'NewPostsTA.html', {'form' : form })

@login_required
def modificar_PostTA(request, codigo):
	carrera = get_object_or_404(PostTA, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormTA(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormTA(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			return redirect(to='PostTAss')
		data["form"]=formulario	
	return render(request, 'modificar_PostTA.html', data)

@login_required
def modificar_PostTA2(request, codigo):
	carrera = get_object_or_404(PostTA, codigo=codigo)#busca un elemento

	data={ 'form' : PostFormTA(instance=carrera)}

	if request.method=='POST':
		formulario=PostFormTA(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request, f"Comentario Editado Correctamente")
			usern = carrera.user
			return redirect('PostsPedidos', username=usern)
		data["form"]=formulario	
	return render(request, 'modificar_PostTA2.html', data)

@login_required
def eliminar_PostTA(request, codigo):
	carrera = get_object_or_404(PostTA, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	return redirect(to="PostTAss")

@login_required
def eliminar_PostTA2(request, codigo):
	carrera = get_object_or_404(PostTA, codigo=codigo)
	carrera.delete()
	messages.success(request, f"Comentario Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

#########################-Usuarios-##############################

@login_required
def contactar(request):
	if request.method=="POST":
		asunto=request.POST["txtAsunto"]
		mensaje="Email: " + request.POST["txtEmail"] + " / Nombre: " + request.user.first_name + " / Mensaje: " + request.POST["txtMensaje"]
		email_desde=settings.EMAIL_HOST_USER
		email_para=["Beyourself11b@gmail.com"]
		send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
		messages.success(request, 'Email Enviado Correctamente')
		return redirect(to='contactar')

	return render(request, "contactar.html")


def registrar_usuario(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			EMAIL = form.cleaned_data['email']
			Nombre = form.cleaned_data['first_name']
			messages.success(request, f'Usuario {username} creado')
			#template = render_to_string('email_template.html', {'name':request.user.first_name})

			#email = EmailMessage(
			#	'Bienvenido a BeYourSelf',
			#	template,
			#	settings.EMAIL_HOST_USER,
			#	EMAIL,
			#	)

			#email.fail_silently=False
			#email.send()
			return redirect(to='login')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'registrar_usuario.html', context)


@login_required
def EditImagenPersonales(request, codigo):
	carrera=get_object_or_404(Profile, codigo=codigo)#busca un elemento

	data={ 'form' : EditImageForm(instance=carrera)}

	if request.method=='POST':
		formulario=EditImageForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			usern = carrera.user
			messages.success(request, f"Imagen de Perfil Modificado Correctamente")
			return redirect('profile', username=usern)
		data["form"]=formulario
	return render(request, 'EditarImagen.html', data)


@login_required
def AñadirDatos(request, codigo):	
	carrera=get_object_or_404(Profile, codigo=codigo)#busca un elemento
	usuario = carrera.user

	data={ 'form' : AñadirForm(instance=carrera)}

	if request.method=='POST':
		formulario=AñadirForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			usern = carrera.user
			messages.success(request, f"Datos Guardado Correctamente")
			return redirect('profile', username=usern)
		data["form"]=formulario
	return render(request, 'EAñadirDatosP.html', data)


@login_required
def EditDatosPersonales(request, username):
	carrera=get_object_or_404(User, username=username)#busca un elemento

	data={ 'form' : EditUserForm(instance=carrera)}

	if request.method=='POST':
		formulario=EditUserForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			to_user = User.objects.get(username=username)			
			user = formulario.cleaned_data['first_name']
			messages.success(request, f"Datos Personales Modificado Correctamente")
			return redirect('profile', username=to_user)
		data["form"]=formulario
	return render(request, 'EditarUser.html', data)

@login_required
def EditUsuario(request, username):
	carrera=get_object_or_404(User, username=username)#busca un elemento

	data={ 'form' : EditUsuarioForm(instance=carrera)}

	if request.method=='POST':
		formulario=EditUsuarioForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			user = formulario.cleaned_data['username']
			messages.success(request, f"Usuario {user} Modificado Correctamente")
			return redirect(to='logout')
		data["form"]=formulario
	return render(request, 'EditarUsuario.html', data)


########################-Pedir Musica-##############################

@login_required
def VerPMusica(request):

	Musica = Pedir_Musica.objects.all()
	Musi_count = Musica.count()
	myfilter = PedirMusicaFilter(request.GET, queryset=Musica)
	Musica = myfilter.qs

	context = { 'Musica': Musica, 'Musi_count': Musi_count, 'myfilter': myfilter }
	return render(request, 'VerPMusica.html', context)


@login_required
def Pedir_invMusica(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = pedirMusica(request.POST)
		if form.is_valid():				
			det = Pedir_Musica()
			det.pedir = form.cleaned_data['pedir']
			det.material = form.cleaned_data['material']
			if det.pedir > det.material.disponible:
				form = pedirMusica()				
				messages.error(request, f'La cantidad maximo de {det.material} que tenemos para tu solicitud es: {det.material.disponible}')
			else:
				post = form.save(commit=False)
				post.user = current_user
				post.save()
				det.material.disponible -= det.pedir
				det.material.save()
				title = form.cleaned_data['material']			
				description = form.cleaned_data['pedir']			
				start_time = form.cleaned_data['Fecha_a_Pedir']
				end_time = form.cleaned_data['Fecha_Limite']
				Event.objects.create(
					user=request.user,
    				title=title,
    				description=description,
    				start_time=start_time,
    				end_time=end_time
				)		
				messages.success(request, f'Pedido enviado correctamente. Ahora tu pedido se puede visualizar en una sección llamada Calendario, para que puedas tener presente tu pedido y nosotros tambien. ')
				return redirect(to='InventarioMusica')
	else:
		form = pedirMusica()
	return render(request, 'Pedirmusica.html', {'form' : form })

@login_required
def eliminar_PedidoMusi(request, codigo):
	carrera = get_object_or_404(Pedir_Musica, codigo=codigo)
	det = Inv_Musica()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	Use = carrera.material
	Us = carrera.user
	messages.success(request, f"Pedido: {Us}/{Use} Eliminado Correctamente")
	return redirect(to="VerPMusica")

@login_required
def eliminar_PedidoMusi2(request, codigo):
	carrera = get_object_or_404(Pedir_Musica, codigo=codigo)
	det = Inv_Musica()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	messages.success(request, f"Pedido Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)
	
########################-Pedir Pintura-##############################


@login_required
def VerPPintura(request):

	Pintura = Pedir_Pintura.objects.all()
	myfilter = PedirPinturaFilter(request.GET, queryset=Pintura)
	Pintura = myfilter.qs

	context = { 'Pintura': Pintura, 'myfilter': myfilter }
	return render(request, 'VerPPintura.html', context)

@login_required
def Pedir_invPintura(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = pedirPintura(request.POST)
		if form.is_valid():
			det = Pedir_Pintura()
			det.pedir = form.cleaned_data['pedir']
			det.material = form.cleaned_data['material']
			if det.pedir > det.material.disponible:
				form = pedirPintura()				
				messages.error(request, f'La cantidad maximo de {det.material} que tenemos para tu solicitud es: {det.material.disponible}')
			else:
				post = form.save(commit=False)
				post.user = current_user
				post.save()
				det.material.disponible -= det.pedir
				det.material.save()
				title = form.cleaned_data['material']			
				description = form.cleaned_data['pedir']			
				start_time = form.cleaned_data['Fecha_a_Pedir']
				end_time = form.cleaned_data['Fecha_Limite']
				Event.objects.create(
					user=request.user,
    				title=title,
    				description=description,
    				start_time=start_time,
    				end_time=end_time
				)
				messages.success(request, f'Pedido enviado correctamente. Ahora tu pedido se puede visualizar en una sección llamada Calendario, para que puedas tener presente tu pedido y nosotros tambien. ')
				return redirect(to='InventarioPintura')
	else:
		form = pedirPintura()
	return render(request, 'Pedirpintura.html', {'form' : form })

@login_required
def eliminar_PedidoPint(request, codigo):
	carrera = get_object_or_404(Pedir_Pintura, codigo=codigo)
	det = Inv_Pintura()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	Use = carrera.material
	Us = carrera.user
	messages.success(request, f"Pedido: {Us}/{Use} Eliminado Correctamente")
	return redirect(to="VerPPintura")

@login_required
def eliminar_PedidoPint2(request, codigo):
	carrera = get_object_or_404(Pedir_Pintura, codigo=codigo)
	det = Inv_Pintura()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	messages.success(request, f"Pedido Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

########################-Pedir Expresion Corporal-##############################

@login_required
def VerPTA(request):

	TA = Pedir_TA.objects.all()
	myfilter = PedirTAFilter(request.GET, queryset=TA)
	TA = myfilter.qs

	context = { 'TA': TA, 'myfilter': myfilter }
	return render(request, 'VerPTA.html', context)

@login_required
def Pedir_InvTA(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = pedirTA(request.POST)
		if form.is_valid():
			det = Pedir_TA()
			det.pedir = form.cleaned_data['pedir']
			det.material = form.cleaned_data['material']
			if det.pedir > det.material.disponible:
				form = pedirTA()				
				messages.error(request, f'La cantidad maximo de {det.material} que tenemos para tu solicitud es: {det.material.disponible}')
			else:
				post = form.save(commit=False)
				post.user = current_user
				post.save()
				det.material.disponible -= det.pedir
				det.material.save()
				title = form.cleaned_data['material']			
				description = form.cleaned_data['pedir']			
				start_time = form.cleaned_data['Fecha_a_Pedir']
				end_time = form.cleaned_data['Fecha_Limite']
				Event.objects.create(
					user=request.user,
    				title=title,
    				description=description,
    				start_time=start_time,
    				end_time=end_time
				)
				messages.success(request, f'Pedido enviado correctamente. Ahora tu pedido se puede visualizar en una sección llamada Calendario, para que puedas tener presente tu pedido y nosotros tambien. ')
				return redirect(to='InventarioTA')
	else:
		form = pedirTA()
	return render(request, 'PedirTA.html', {'form' : form })

@login_required
def eliminar_PedidoTA(request, codigo):
	carrera = get_object_or_404(Pedir_TA, codigo=codigo)
	det = Inv_TA()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	Use = carrera.material
	Us = carrera.user
	messages.success(request, f"Pedido: {Us}/{Use} Eliminado Correctamente")
	return redirect(to="VerPTA")

@login_required
def eliminar_PedidoTA2(request, codigo):
	carrera = get_object_or_404(Pedir_TA, codigo=codigo)
	det = Inv_TA()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	messages.success(request, f"Pedido Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

########################-Pedir Deportes-##############################

@login_required
def VerPDeportes(request):

	Deportes = Pedir_Deportes.objects.all()
	myfilter = PedirDeportesFilter(request.GET, queryset=Deportes)
	Deportes = myfilter.qs

	context = { 'Deportes': Deportes, 'myfilter': myfilter }
	return render(request, 'VerPDeportes.html', context)

@login_required
def Pedir_InvDeportes(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = pedirDeportes(request.POST)
		if form.is_valid():
			det = Pedir_Deportes()
			det.pedir = form.cleaned_data['pedir']
			det.material = form.cleaned_data['material']
			if det.pedir > det.material.disponible:
				form = pedirDeportes()				
				messages.error(request, f'La cantidad maximo de {det.material} que tenemos para tu solicitud es: {det.material.disponible}')
			else:
				post = form.save(commit=False)
				post.user = current_user
				post.save()
				det.material.disponible -= det.pedir
				det.material.save()
				title = form.cleaned_data['material']			
				description = form.cleaned_data['pedir']			
				start_time = form.cleaned_data['Fecha_a_Pedir']
				end_time = form.cleaned_data['Fecha_Limite']
				Event.objects.create(
					user=request.user,
    				title=title,
    				description=description,
    				start_time=start_time,
    				end_time=end_time
				)
				messages.success(request, f'Pedido enviado correctamente. Ahora tu pedido se puede visualizar en una sección llamada Calendario, para que puedas tener presente tu pedido y nosotros tambien. ')
				return redirect(to='InventarioDeportes')
	else:
		form = pedirDeportes()
	return render(request, 'PedirDeportes.html', {'form' : form })

@login_required
def eliminar_PedidoDepo(request, codigo):
	carrera = get_object_or_404(Pedir_Deportes, codigo=codigo)
	det = Inv_Deportes()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	Use = carrera.material
	Us = carrera.user
	messages.success(request, f"Pedido: {Us}/{Use} Eliminado Correctamente")
	return redirect(to="VerPDeportes")

@login_required
def eliminar_PedidoDepo2(request, codigo):
	carrera = get_object_or_404(Pedir_Deportes, codigo=codigo)
	det = Inv_Deportes()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	messages.success(request, f"Pedido Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)

########################-Pedir Danzas-##############################

@login_required
def VerPDanzas(request):

	Danzas = Pedir_Danzas.objects.all()
	myfilter = PedirDanzasFilter(request.GET, queryset=Danzas)
	Danzas = myfilter.qs

	context = { 'Danzas': Danzas, 'myfilter': myfilter }
	return render(request, 'VerPDanzas.html', context)


@login_required
def Pedir_InvDanzas(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = pedirDanzas(request.POST)
		if form.is_valid():
			det = Pedir_Danzas()
			det.pedir = form.cleaned_data['pedir']
			det.material = form.cleaned_data['material']
			if det.pedir > det.material.disponible:
				form = pedirDanzas()				
				messages.error(request, f'La cantidad maximo de {det.material} que tenemos para tu solicitud es: {det.material.disponible}')
			else:
				post = form.save(commit=False)
				post.user = current_user
				post.save()
				det.material.disponible -= det.pedir
				det.material.save()
				title = form.cleaned_data['material']			
				description = form.cleaned_data['pedir']			
				start_time = form.cleaned_data['Fecha_a_Pedir']
				end_time = form.cleaned_data['Fecha_Limite']
				Event.objects.create(
					user=request.user,
    				title=title,
    				description=description,
    				start_time=start_time,
    				end_time=end_time
				)
				messages.success(request, f'Pedido enviado correctamente. Ahora tu pedido se puede visualizar en una sección llamada Calendario, para que puedas tener presente tu pedido y nosotros tambien. ')
				return redirect(to='InventarioDanzas')
	else:
		form = pedirDanzas()
	return render(request, 'PedirDanzas.html', {'form' : form })

@login_required
def eliminar_PedidoDanza(request, codigo):
	carrera = get_object_or_404(Pedir_Danzas, codigo=codigo)
	det = Inv_Danzas()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	Use = carrera.material
	Us = carrera.user
	messages.success(request, f"Pedido: {Us}/{Use} Eliminado Correctamente")
	return redirect(to="VerPDanzas")

@login_required
def eliminar_PedidoDanza2(request, codigo):
	carrera = get_object_or_404(Pedir_Danzas, codigo=codigo)
	det = Inv_Danzas()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	messages.success(request, f"Pedido Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)
	

########################-Pedir Fotografia-##############################

@login_required
def VerPFoto(request):

	Foto = Pedir_Foto.objects.all()
	myfilter = PedirFotoFilter(request.GET, queryset=Foto)
	Foto = myfilter.qs

	context = { 'Foto': Foto, 'myfilter': myfilter }
	return render(request, 'VerPFoto.html', context)

@login_required
def Pedir_InvFoto(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = pedirFoto(request.POST)
		if form.is_valid():
			det = Pedir_Foto()
			det.pedir = form.cleaned_data['pedir']
			det.material = form.cleaned_data['material']
			if det.pedir > det.material.disponible:
				form = pedirFoto()				
				messages.error(request, f'La cantidad maximo de {det.material} que tenemos para tu solicitud es: {det.material.disponible}')
			else:
				post = form.save(commit=False)
				post.user = current_user
				post.save()
				det.material.disponible -= det.pedir
				det.material.save()
				title = form.cleaned_data['material']			
				description = form.cleaned_data['pedir']			
				start_time = form.cleaned_data['Fecha_a_Pedir']
				end_time = form.cleaned_data['Fecha_Limite']
				Event.objects.create(
					user=request.user,
    				title=title,
    				description=description,
    				start_time=start_time,
    				end_time=end_time
				)
				messages.success(request, f'Pedido enviado correctamente. Ahora tu pedido se puede visualizar en una sección llamada Calendario, para que puedas tener presente tu pedido y nosotros tambien. ')
				return redirect(to='InventarioFotografia')
	else:
		form = pedirFoto()
	return render(request, 'PedirFoto.html', {'form' : form })

@login_required
def eliminar_PedidoFoto(request, codigo):
	carrera = get_object_or_404(Pedir_Foto, codigo=codigo)
	det = Inv_Foto()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	Use = carrera.material
	Us = carrera.user
	messages.success(request, f"Pedido: {Us}/{Use} Eliminado Correctamente")
	return redirect(to="VerPFoto")

@login_required
def eliminar_PedidoFoto2(request, codigo):
	carrera = get_object_or_404(Pedir_Foto, codigo=codigo)
	det = Inv_Foto()
	det.materialess = carrera.material
	det.materialess.disponible += carrera.pedir
	det.materialess.save()
	carrera.delete()
	messages.success(request, f"Pedido Eliminado Correctamente")
	usern = carrera.user
	return redirect('PostsPedidos', username=usern)
