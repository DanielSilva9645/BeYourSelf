from django.contrib import admin
from Modulos.Principal.models import *

@admin.register(LOGOS)
class LogosAdmin(admin.ModelAdmin):
	ordering = ('image',)
	list_display = ('image',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	ordering = ('user',)
	list_display = ('user', 'title', 'description', 'start_time', 'end_time', 'created_date',)

@admin.register(Profile)
class ProfileaAdmin(admin.ModelAdmin):
	ordering = ('user',)
	list_display = ('user', 'image', 'Celular', 'Telefono',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	ordering = ('timestamp',)
	list_display = ('timestamp', 'codigo', 'user', 'content', 'image',)

@admin.register(PostFotografia)
class PostFotografiaAdmin(admin.ModelAdmin):
	ordering = ('timestamp',)
	list_display = ('timestamp', 'codigo', 'user', 'content',)

@admin.register(PostDanzas)
class PostDanzasAdmin(admin.ModelAdmin):
	ordering = ('timestamp',)
	list_display = ('timestamp', 'codigo', 'user', 'content',)

@admin.register(PostDeportes)
class PostDeportesAdmin(admin.ModelAdmin):
	ordering = ('timestamp',)
	list_display = ('timestamp', 'codigo', 'user', 'content',)

@admin.register(PostPintura)
class PostPinturaAdmin(admin.ModelAdmin):
	ordering = ('timestamp',)
	list_display = ('timestamp', 'codigo', 'user', 'content',)

@admin.register(PostMusica)
class PostMusicaAdmin(admin.ModelAdmin):
	ordering = ('timestamp',)
	list_display = ('timestamp', 'codigo', 'user', 'content',)

@admin.register(PostTA)
class PostTAAdmin(admin.ModelAdmin):
	ordering = ('timestamp',)
	list_display = ('timestamp', 'codigo', 'user', 'content',)
admin.site.register(Relationship)