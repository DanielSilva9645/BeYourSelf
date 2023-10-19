from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.urls import reverse

class LOGOS(models.Model):
	image = models.ImageField(default='logoCosfa.png')

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripción')
    start_time = models.DateField('Fecha y Hora inicio')
    end_time = models.DateField('Fecha y Hora final   ')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class Profile(models.Model):
	codigo = models.AutoField(primary_key=True, default=None)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='perfiles/user_3.png',upload_to="perfiles/", null=True, blank=True)
	TD=[
		('Cedula', 'Cedula'),
		('Tarjeta de Identidad', 'Tarjeta de Identidad')
	]
	Tipo_de_Documento_de_Identidad = models.CharField(max_length=20, choices=TD, default='Tarjeta de Identidad')
	Numero_de_Documento_de_Identidad = models.CharField(max_length=10, default='')
	Celular = models.CharField(max_length=10, default='')
	Telefono = models.CharField(max_length=7, default='')

	def __str__(self):
		return f'Perfil de {self.user.username}'

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user)\
								.values_list('to_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user)\
								.values_list('from_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
		

class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} sigue a {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]


class Post(models.Model):
	codigo = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateField(default=timezone.now)
	content = models.TextField()
	image = models.FileField(upload_to="archivos/", null=True, blank=True)

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'

class PostFotografia(models.Model):
	codigo = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postsFoto')
	timestamp = models.DateField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'

class PostDanzas(models.Model):
	codigo = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postsDanzas')
	timestamp = models.DateField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'

class PostDeportes(models.Model):
	codigo = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postsDepo')
	timestamp = models.DateField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'

class PostPintura(models.Model):
	codigo = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postsPint')
	timestamp = models.DateField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'

class PostMusica(models.Model):
	codigo = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postsMusi')
	timestamp = models.DateField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'

class PostTA(models.Model):
	codigo = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postsTA')
	timestamp = models.DateField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'
	
		
