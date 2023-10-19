from django.contrib import admin
from Modulos.Academico.models import *

# Register your models here.

@admin.register(Pedir_Musica)
class Pedir_MusicaAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'user', 'material', 'pedir', 'Fecha_Solicitado', 'Fecha_a_Pedir', 'Fecha_Limite',)

@admin.register(Inv_Musica)
class Inv_MusicaAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'materialess', 'disponible', 'Estado',)

############################################################################

@admin.register(Pedir_Pintura)
class Pedir_PinturaAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'user', 'material', 'pedir', 'Fecha_Solicitado', 'Fecha_a_Pedir', 'Fecha_Limite',)

@admin.register(Inv_Pintura)
class Inv_PinturaAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'materialess', 'disponible', 'Estado',)

############################################################################

@admin.register(Pedir_TA)
class Pedir_TAAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'user', 'material', 'pedir', 'Fecha_Solicitado', 'Fecha_a_Pedir', 'Fecha_Limite',)

@admin.register(Inv_TA)
class Inv_TAAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'materialess', 'disponible', 'Estado',)

############################################################################

@admin.register(Pedir_Deportes)
class Pedir_DeportesAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'user', 'material', 'pedir', 'Fecha_Solicitado', 'Fecha_a_Pedir', 'Fecha_Limite',)

@admin.register(Inv_Deportes)
class Inv_DeportesAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'materialess', 'disponible', 'Estado',)

############################################################################

@admin.register(Pedir_Danzas)
class Pedir_DanzasAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'user', 'material', 'pedir', 'Fecha_Solicitado', 'Fecha_a_Pedir', 'Fecha_Limite',)

@admin.register(Inv_Danzas)
class Inv_DanzasAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'materialess', 'disponible', 'Estado',)

############################################################################

@admin.register(Pedir_Foto)
class Pedir_DanzasAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'user', 'material', 'pedir', 'Fecha_Solicitado', 'Fecha_a_Pedir', 'Fecha_Limite',)

@admin.register(Inv_Foto)
class Inv_FotoAdmin(admin.ModelAdmin):
	ordering = ('codigo',)
	list_display = ('codigo', 'materialess', 'disponible', 'Estado',)

