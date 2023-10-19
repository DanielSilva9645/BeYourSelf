import django_filters
from django_filters import *
from django.forms import DateInput

from .models import *
from Modulos.Academico.models import *

########################################## Posts ##########################################

class PostFilter(django_filters.FilterSet):
	content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

	class Meta:
		model = Post
		fields = '__all__'
		exclude = ['image']
		

class PostFotoFilter(django_filters.FilterSet):
	content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

	class Meta:
		model = PostFotografia
		fields = '__all__'


class PostDanzasFilter(django_filters.FilterSet):
	content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

	class Meta:
		model = PostDanzas
		fields = '__all__'


class PostDepoFilter(django_filters.FilterSet):
	content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

	class Meta:
		model = PostDeportes
		fields = '__all__'


class PostPintFilter(django_filters.FilterSet):
	content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

	class Meta:
		model = PostPintura
		fields = '__all__'


class PostMusiFilter(django_filters.FilterSet):
	content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

	class Meta:
		model = PostMusica
		fields = '__all__'


class PostTAFilter(django_filters.FilterSet):
	content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')

	class Meta:
		model = PostTA
		fields = '__all__'			


########################################## Inventarios ##########################################


class InvMusicaFilter(django_filters.FilterSet):
	materialess = django_filters.CharFilter(field_name='materialess', lookup_expr='icontains')

	class Meta:
		model = Inv_Musica
		fields = '__all__'
		exclude = ['disponible', 'Estado']


class InvPinturaFilter(django_filters.FilterSet):
	materialess = django_filters.CharFilter(field_name='materialess', lookup_expr='icontains')

	class Meta:
		model = Inv_Pintura
		fields = '__all__'
		exclude = ['disponible', 'Estado']


class InvTAFilter(django_filters.FilterSet):
	materialess = django_filters.CharFilter(field_name='materialess', lookup_expr='icontains')

	class Meta:
		model = Inv_TA
		fields = '__all__'
		exclude = ['disponible', 'Estado']


class InvDeportesFilter(django_filters.FilterSet):
	materialess = django_filters.CharFilter(field_name='materialess', lookup_expr='icontains')

	class Meta:
		model = Inv_Deportes
		fields = '__all__'
		exclude = ['disponible', 'Estado']


class InvDanzasFilter(django_filters.FilterSet):
	materialess = django_filters.CharFilter(field_name='materialess', lookup_expr='icontains')

	class Meta:
		model = Inv_Danzas
		fields = '__all__'
		exclude = ['disponible', 'Estado']


class InvFotoFilter(django_filters.FilterSet):
	materialess = django_filters.CharFilter(field_name='materialess', lookup_expr='icontains')

	class Meta:
		model = Inv_Foto
		fields = '__all__'
		exclude = ['disponible', 'Estado']


########################################## Pedidos ##########################################


class PedirMusicaFilter(django_filters.FilterSet):

	class Meta:
		model = Pedir_Musica
		fields = '__all__'


class PedirPinturaFilter(django_filters.FilterSet):

	class Meta:
		model = Pedir_Pintura
		fields = '__all__'


class PedirTAFilter(django_filters.FilterSet):

	class Meta:
		model = Pedir_TA
		fields = '__all__'


class PedirDeportesFilter(django_filters.FilterSet):

	class Meta:
		model = Pedir_Deportes
		fields = '__all__'


class PedirDanzasFilter(django_filters.FilterSet):

	class Meta:
		model = Pedir_Danzas
		fields = '__all__'
		exclude = ['disponible', 'Estado']


class PedirFotoFilter(django_filters.FilterSet):

	class Meta:
		model = Pedir_Foto
		fields = '__all__'
