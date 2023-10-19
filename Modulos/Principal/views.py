import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .models import *
from .utils import Calendar
from .forms import EventForm
from Modulos.Academico.models import *
from Modulos.Academico.forms import *
from .filters import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, View
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from datetime import datetime, date, timedelta
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#Create your views here.

@login_required
def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		postsFoto = user.postsFoto.all()
		postsDanzas = user.postsDanzas.all()
		postsDepo = user.postsDepo.all()
		postsPint = user.postsPint.all()
		postsMusi = user.postsMusi.all()
		postsTA = user.postsTA.all()

		HFoto = user.HFoto.all()
		HDanzas = user.HDanzas.all()
		HDepo = user.HDepo.all()
		HPint = user.HPint.all()
		HMusi = user.HMusi.all()
		HTA = user.HTA.all()

	else:
		postsFoto = current_user.postsFoto.all()
		postsDanzas = current_user.postsDanzas.all()
		postsDepo = current_user.postsDepo.all()
		postsPint = current_user.postsPint.all()
		postsMusi = current_user.postsMusi.all()
		postsTA = current_user.postsTA.all()
		user = current_user

		HFoto = current_user.HFoto.all()
		HDanzas = current_user.HDanzas.all()
		HDepo = current_user.HDepo.all()
		HPint = current_user.HPint.all()
		HMusi = current_user.HMusi.all()
		HTA = current_user.HTA.all()

	return render(request, 'Profile.html', {'user':user, 
	'postsFoto':postsFoto, 'postsDanzas':postsDanzas, 
	'postsDepo':postsDepo, 'postsPint':postsPint,
	'postsMusi':postsMusi, 'postsTA':postsTA,
	'HFoto':HFoto, 'HDanzas':HDanzas,
	'HDepo':HDepo, 'HPint':HPint,
	'HMusi':HMusi, 'HTA':HTA})

@login_required
def PostsPedidos(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		postsFoto = user.postsFoto.all()
		postsDanzas = user.postsDanzas.all()
		postsDepo = user.postsDepo.all()
		postsPint = user.postsPint.all()
		postsMusi = user.postsMusi.all()
		postsTA = user.postsTA.all()

		HFoto = user.HFoto.all()
		HDanzas = user.HDanzas.all()
		HDepo = user.HDepo.all()
		HPint = user.HPint.all()
		HMusi = user.HMusi.all()
		HTA = user.HTA.all()

	else:
		postsFoto = current_user.postsFoto.all()
		postsDanzas = current_user.postsDanzas.all()
		postsDepo = current_user.postsDepo.all()
		postsPint = current_user.postsPint.all()
		postsMusi = current_user.postsMusi.all()
		postsTA = current_user.postsTA.all()
		user = current_user

		HFoto = current_user.HFoto.all()
		HDanzas = current_user.HDanzas.all()
		HDepo = current_user.HDepo.all()
		HPint = current_user.HPint.all()
		HMusi = current_user.HMusi.all()
		HTA = current_user.HTA.all()

	return render(request, 'PostsPedidos.html', {'user':user, 
	'postsFoto':postsFoto, 'postsDanzas':postsDanzas, 
	'postsDepo':postsDepo, 'postsPint':postsPint,
	'postsMusi':postsMusi, 'postsTA':postsTA,
	'HFoto':HFoto, 'HDanzas':HDanzas,
	'HDepo':HDepo, 'HPint':HPint,
	'HMusi':HMusi, 'HTA':HTA})

@login_required
def ViewFollow(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		relationships = user.relationships.all()
		related_to = user.related_to.all()
	else:
		relationships = current_user.relationships.all()
		related_to = current_user.related_to.all()
		user = current_user
	return render(request, 'Follows.html', {'user':user, 'relationships':relationships,
	'related_to':related_to})

@login_required
def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a @{username}')
	return redirect('profile', username=to_user)

@login_required
def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a @{username}')
	return redirect('profile', username=to_user)


@login_required
def IndexView(request):
	return render(request, 'index.html')

@login_required
def Area_Personal(request):
	return render(request, 'AreaPersonal.html')

@login_required
def Inventarios(request):
	return render(request, 'inventarios.html')


def Presentacion(request):
	return render(request, 'presentacion.html')

#########################-Calendario-#########################

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

@login_required
def create_event(request):    
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time
        )
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event.html', {'form': form})

class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'eventedit.html'


@login_required()
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        'event': event
    }
    return render(request, 'event-details.html', context)


class eliminar_evento(generic.DeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('calendar')


#########################-Inventario Musica-#########################	

@login_required
def listadosInvMusica(request):
	listadosInvMusica=Inv_Musica.objects.filter(disponible__gt=0)
	myfilter = InvMusicaFilter(request.GET, queryset=listadosInvMusica)
	listadosInvMusica = myfilter.qs

	return render(request, "InventarioMusica.html",{"InvMusica":listadosInvMusica,
		'myfilter': myfilter })

@login_required
def AgregarInvMusica(request):
	data={
		'form': MusiForm()
	}
	if request.method =='POST':
		formulario = MusiForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f'{material} Agregado Correctamente')
			return redirect(to='InventarioMusica')
		else:
			data["form"]=formulario
			messages.success(request, f'Articulo Ya existe')
	return render(request, 'AgregarInvMusica.html', data)

@login_required
def modificar_InvMusica(request, codigo):
	carrera=get_object_or_404(Inv_Musica, codigo=codigo)#busca un elemento

	data={ 'form' : MusiForm(instance=carrera)}

	if request.method=='POST':
		formulario=MusiForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f"{material} Modificado Correctamente")
			return redirect(to='InventarioMusica')
		data["form"]=formulario	
	return render(request, 'modificarMusica.html', data)

@login_required
def eliminar_InvMusica(request, codigo):
	carrera = get_object_or_404(Inv_Musica, codigo=codigo)
	carrera.delete()
	messages.success(request, f" Eliminado Correctamente")
	return redirect(to="InventarioMusica")

@login_required
def InvMusica_reportepdf(request):
	Musica=Inv_Musica.objects.all()
	logo=LOGOS.objects.all()
	template_path="PDF-InvMusica.html"
	context ={'Musica':Musica,
		'logo': logo
		}
	response=HttpResponse(content_type='application/pdf')
	#response['Content-Disposition']='attachment; filename="PDF-InvMusica.pdf"'
	template=get_template('PDF-InvMusica.html')
	html=template.render(context)
	pisa_status=pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('Se presentaron algunos problemas <pre>' + html + '</pre>')
	return response


#########################-Inventario Pintura-#########################	

@login_required
def listadosInvPintura(request):
	listadosInvPintura=Inv_Pintura.objects.filter(disponible__gt=0)
	myfilter = InvPinturaFilter(request.GET, queryset=listadosInvPintura)
	listadosInvPintura = myfilter.qs

	return render(request, "InventarioPintura.html",{"InvPintura":listadosInvPintura, 
		'myfilter': myfilter })

@login_required
def AgregarInvPintura(request):
	data={
		'form': PintForm()
	}
	if request.method =='POST':
		formulario = PintForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f'{material} Agregado Correctamente')
			return redirect(to='InventarioPintura')
		else:
			data["form"]=formulario
			messages.success(request, f'Articulo Ya existe')
	return render(request, 'AgregarInvPint.html', data)


@login_required
def modificar_InvPintura(request, codigo):
	carrera=get_object_or_404(Inv_Pintura, codigo=codigo)#busca un elemento

	data={ 'form' : PintForm(instance=carrera)}

	if request.method=='POST':
		formulario=PintForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f"{material} Modificado Correctamente")
			return redirect(to='InventarioPintura')
		data["form"]=formulario
	return render(request, 'modificarPint.html', data)

@login_required
def eliminar_InvPintura(request, codigo):
	carrera = get_object_or_404(Inv_Pintura, codigo=codigo)
	carrera.delete()
	messages.success(request, "Eliminado Correctamente")
	return redirect(to="InventarioPintura")

@login_required
def Inv_Pintura_reportepdf(request):
	Pintura=Inv_Pintura.objects.all()
	logo=LOGOS.objects.all()
	template_path="PDF-InvPintura.html"
	context ={'Pintura':Pintura,
		'logo': logo
		}
	response=HttpResponse(content_type='application/pdf')
	#response['Content-Disposition']='attachment; filename="PDF-InvPintura.pdf"'
	template=get_template('PDF-InvPintura.html')
	html=template.render(context)
	pisa_status=pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('Se presentaron algunos problemas <pre>' + html + '</pre>')
	return response

#########################-Inventario Teatro AudioVisuales-#########################	

@login_required
def listadosInvTA(request):
	listadosInvTA=Inv_TA.objects.filter(disponible__gt=0)
	myfilter = InvTAFilter(request.GET, queryset=listadosInvTA)
	listadosInvTA = myfilter.qs

	return render(request, "InventarioTA.html",{"InvTA":listadosInvTA,
		'myfilter': myfilter })

@login_required
def AgregarInvTA(request):
	data={
		'form': TAForm()
	}
	if request.method =='POST':
		formulario = TAForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f'{material} Agregado Correctamente')
			return redirect(to='InventarioTA')
		else:
			data["form"]=formulario
			messages.success(request, f'Articulo Ya existe')
	return render(request, 'AgregarInvTA.html', data)


@login_required
def modificar_InvTA(request, codigo):
	carrera=get_object_or_404(Inv_TA, codigo=codigo)#busca un elemento

	data={ 'form' : TAForm(instance=carrera)}

	if request.method=='POST':
		formulario=TAForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f"{material} Modificado Correctamente")
			return redirect(to='InventarioTA')
		data["form"]=formulario
	return render(request, 'modificarTA.html', data)

@login_required
def eliminar_InvTA(request, codigo):
	carrera = get_object_or_404(Inv_TA, codigo=codigo)
	carrera.delete()
	messages.success(request, "Eliminado Correctamente")
	return redirect(to="InventarioTA")

@login_required
def Inv_TA_reportepdf(request):
	TA=Inv_TA.objects.all()
	logo=LOGOS.objects.all()
	template_path="PDF-InvTA.html"
	context ={'TA':TA,
		'logo': logo
		}
	response=HttpResponse(content_type='application/pdf')
	#response['Content-Disposition']='attachment; filename="PDF-InvTA.pdf"'
	template=get_template('PDF-InvTA.html')
	html=template.render(context)
	pisa_status=pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('Se presentaron algunos problemas <pre>' + html + '</pre>')
	return response


#########################-Inventario Deportes-#########################	

@login_required
def listadosInvDeportes(request):
	listadosInvDeportes=Inv_Deportes.objects.filter(disponible__gt=0)
	myfilter = InvDeportesFilter(request.GET, queryset=listadosInvDeportes)
	listadosInvDeportes = myfilter.qs

	return render(request, "InventarioDeportes.html",{"InvDeportes":listadosInvDeportes,
		'myfilter': myfilter })

@login_required
def AgregarInvDepo(request):
	data={
		'form': DeportesForm()
	}
	if request.method =='POST':
		formulario = DeportesForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f'{material} Agregado Correctamente')
			return redirect(to='InventarioDeportes')
		else:
			data["form"]=formulario
			messages.success(request, f'Articulo Ya existe')
	return render(request, 'AgregarInvDepo.html', data)


@login_required
def modificar_InvDepo(request, codigo):
	carrera=get_object_or_404(Inv_Deportes, codigo=codigo)#busca un elemento

	data={ 'form' : DeportesForm(instance=carrera)}

	if request.method=='POST':
		formulario=DeportesForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f"{material} Modificado Correctamente")
			return redirect(to='InventarioDeportes')
		data["form"]=formulario
	return render(request, 'modificarDepo.html', data)

@login_required
def eliminar_InvDepo(request, codigo):
	carrera = get_object_or_404(Inv_Deportes, codigo=codigo)
	carrera.delete()
	messages.success(request, "Eliminado Correctamente")
	return redirect(to="InventarioDeportes")

@login_required
def Inv_Deportes_reportepdf(request):
	Deportes=Inv_Deportes.objects.all()
	logo=LOGOS.objects.all()
	template_path="PDF-InvDepo.html"
	context ={'Deportes':Deportes,
		'logo': logo
		}
	response=HttpResponse(content_type='application/pdf')
	#response['Content-Disposition']='attachment; filename="PDF-InvDepo.pdf"'
	template=get_template('PDF-InvDepo.html')
	html=template.render(context)
	pisa_status=pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('Se presentaron algunos problemas <pre>' + html + '</pre>')
	return response


#########################-Inventario Danzas-#########################	

@login_required
def listadosInvDanzas(request):
	listadosInvDanzas=Inv_Danzas.objects.filter(disponible__gt=0)
	myfilter = InvDanzasFilter(request.GET, queryset=listadosInvDanzas)
	listadosInvDanzas = myfilter.qs

	return render(request, "InventarioDanzas.html",{"InvDanzas":listadosInvDanzas,
		'myfilter': myfilter })

@login_required
def AgregarInvDanza(request):
	data={
		'form': DanzasForm()
	}
	if request.method =='POST':
		formulario = DanzasForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f'{material} Agregado Correctamente')
			return redirect(to='InventarioDanzas')
		else:
			data["form"]=formulario
			messages.success(request, f'Articulo Ya existe')
	return render(request, 'AgregarInvDanza.html', data)

@login_required
def modificar_InvDanza(request, codigo):
	carrera=get_object_or_404(Inv_Danzas, codigo=codigo)#busca un elemento

	data={ 'form' : DanzasForm(instance=carrera)}

	if request.method=='POST':
		formulario=DanzasForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f"{material} Modificado Correctamente")
			return redirect(to='InventarioDanzas')
		data["form"]=formulario
	return render(request, 'modificarDanza.html', data)

@login_required
def eliminar_InvDanza(request, codigo):
	carrera = get_object_or_404(Inv_Danzas, codigo=codigo)
	carrera.delete()
	messages.success(request, "Eliminado Correctamente")
	return redirect(to="InventarioDanzas")

@login_required
def Inv_Danzas_reportepdf(request):
	Danzas=Inv_Danzas.objects.all()
	logo=LOGOS.objects.all()
	template_path="PDF-InvDanza.html"
	context ={'Danzas':Danzas,
		'logo': logo
		}
	response=HttpResponse(content_type='application/pdf')
	#response['Content-Disposition']='attachment; filename="PDF-InvDanza.pdf"'
	template=get_template('PDF-InvDanza.html')
	html=template.render(context)
	pisa_status=pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('Se presentaron algunos problemas <pre>' + html + '</pre>')
	return response

#########################-Inventario Fotografia-#########################	

@login_required
def listadosInvFoto(request):
	listadosInvFoto=Inv_Foto.objects.filter(disponible__gt=0)
	myfilter = InvFotoFilter(request.GET, queryset=listadosInvFoto)
	listadosInvFoto = myfilter.qs
	
	return render(request, "InventarioFotografia.html",{"InvFoto":listadosInvFoto,
		'myfilter': myfilter })

@login_required
def AgregarInvFoto(request):
	data={
		'form': FotoForm()
	}
	if request.method =='POST':
		formulario = FotoForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f'{material} Agregado Correctamente')
			return redirect(to='InventarioFotografia')
		else:
			data["form"]=formulario
			messages.success(request, f'Articulo Ya existe')
	return render(request, 'AgregarInvFoto.html', data)

@login_required
def modificar_InvFoto(request, codigo):
	carrera=get_object_or_404(Inv_Foto, codigo=codigo)#busca un elemento

	data={ 'form' : FotoForm(instance=carrera)}

	if request.method=='POST':
		formulario=FotoForm(data=request.POST, instance=carrera, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			material = formulario.cleaned_data['materialess']
			messages.success(request, f"{material} Modificado Correctamente")
			return redirect(to='InventarioFotografia')
		data["form"]=formulario
	return render(request, 'modificarFoto.html', data)

@login_required
def eliminar_InvFoto(request, codigo):
	carrera = get_object_or_404(Inv_Foto, codigo=codigo)
	carrera.delete()
	messages.success(request, "Eliminado Correctamente")
	return redirect(to="InventarioFotografia")

@login_required
def Inv_Foto_reportepdf(request):
	Foto=Inv_Foto.objects.all()
	logo=LOGOS.objects.all()
	template_path="PDF-InvFoto.html"
	context ={'Foto':Foto,
		'logo': logo
		}
	response=HttpResponse(content_type='application/pdf')
	#response['Content-Disposition']='attachment; filename="PDF-InvFoto.pdf"'
	template=get_template('PDF-InvFoto.html')
	html=template.render(context)
	pisa_status=pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('Se presentaron algunos problemas <pre>' + html + '</pre>')
	return response


