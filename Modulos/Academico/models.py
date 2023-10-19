from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Inv_Musica(models.Model):
	codigo=models.AutoField(primary_key=True)
	materialess=models.CharField(max_length=50, default='')
	disponible=models.IntegerField()
	Estado = models.CharField(max_length=10, default='')

	def __str__(self):
		txt="{0}"
		return txt.format(self.materialess)

class Pedir_Musica(models.Model):
	codigo=models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='HMusi')
	material = models.ForeignKey(Inv_Musica, null=False, blank=False, on_delete=models.CASCADE)
	pedir = models.IntegerField()
	Fecha_Solicitado = models.DateTimeField(default=timezone.now)
	Fecha_a_Pedir = models.DateField(default=timezone.now)
	Fecha_Limite = models.DateField(default=timezone.now)

	def __str__(self):
		txt="El dia {0}. El usuario {1} a pedido {2} {3}, Para el {4} hasta el {5}"
		fech0=self.Fecha_Solicitado.strftime("%A-%d/%B/%Y a las %I:%M %p")
		fech1=self.Fecha_a_Pedir.strftime("%A-%d/%B/%Y")
		fech2=self.Fecha_Limite.strftime("%A-%d/%B/%Y")
		return txt.format(fech0, self.user, self.pedir, self.material, fech1, fech2)
		

############################################################################################

class Inv_Pintura(models.Model):
	codigo=models.AutoField(primary_key=True)
	materialess=models.CharField(max_length=50, default='')
	disponible=models.IntegerField()
	Estado = models.CharField(max_length=10, default='')

	def __str__(self):
		txt="{0}"
		return txt.format(self.materialess)

class Pedir_Pintura(models.Model):
	codigo=models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='HPint')
	material = models.ForeignKey(Inv_Pintura, null=False, blank=False, on_delete=models.CASCADE)
	pedir = models.IntegerField()
	Fecha_Solicitado = models.DateTimeField(default=timezone.now)
	Fecha_a_Pedir = models.DateField(default=timezone.now)
	Fecha_Limite = models.DateField(default=timezone.now)

	def __str__(self):
		txt="El dia {0}. El usuario {1} a pedido {2} {3}, Para el {4} hasta el {5}"
		fech0=self.Fecha_Solicitado.strftime("%A-%d/%B/%Y a las %I:%M %p")
		fech1=self.Fecha_a_Pedir.strftime("%A-%d/%B/%Y")
		fech2=self.Fecha_Limite.strftime("%A-%d/%B/%Y")
		return txt.format(fech0, self.user, self.pedir, self.material, fech1, fech2)


############################################################################################

class Inv_TA(models.Model):
	codigo=models.AutoField(primary_key=True)
	materialess=models.CharField(max_length=50, default='')
	disponible=models.IntegerField()
	Estado = models.CharField(max_length=10, default='')

	def __str__(self):
		txt="{0}"
		return txt.format(self.materialess)

class Pedir_TA(models.Model):
	codigo=models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='HTA')
	material = models.ForeignKey(Inv_TA, null=False, blank=False, on_delete=models.CASCADE)
	pedir = models.IntegerField()
	Fecha_Solicitado = models.DateTimeField(default=timezone.now)
	Fecha_a_Pedir = models.DateField(default=timezone.now)
	Fecha_Limite = models.DateField(default=timezone.now)

	def __str__(self):
		txt="El dia {0}. El usuario {1} a pedido {2} {3}, Para el {4} hasta el {5}"
		fech0=self.Fecha_Solicitado.strftime("%A-%d/%B/%Y a las %I:%M %p")
		fech1=self.Fecha_a_Pedir.strftime("%A-%d/%B/%Y")
		fech2=self.Fecha_Limite.strftime("%A-%d/%B/%Y")
		return txt.format(fech0, self.user, self.pedir, self.material, fech1, fech2)


############################################################################################

class Inv_Deportes(models.Model):
	codigo=models.AutoField(primary_key=True)
	materialess=models.CharField(max_length=50, default='')
	disponible=models.IntegerField()
	Estado = models.CharField(max_length=10, default='')

	def __str__(self):
		txt="{0}"
		return txt.format(self.materialess)

class Pedir_Deportes(models.Model):
	codigo=models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='HDepo')
	material = models.ForeignKey(Inv_Deportes, null=False, blank=False, on_delete=models.CASCADE)
	pedir = models.IntegerField()
	Fecha_Solicitado = models.DateTimeField(default=timezone.now)
	Fecha_a_Pedir = models.DateField(default=timezone.now)
	Fecha_Limite = models.DateField(default=timezone.now)

	def __str__(self):
		txt="El dia {0}. El usuario {1} a pedido {2} {3}, Para el {4} hasta el {5}"
		fech0=self.Fecha_Solicitado.strftime("%A-%d/%B/%Y a las %I:%M %p")
		fech1=self.Fecha_a_Pedir.strftime("%A-%d/%B/%Y")
		fech2=self.Fecha_Limite.strftime("%A-%d/%B/%Y")
		return txt.format(fech0, self.user, self.pedir, self.material, fech1, fech2)

############################################################################################

class Inv_Danzas(models.Model):
	codigo=models.AutoField(primary_key=True)
	materialess=models.CharField(max_length=50, default='')
	disponible=models.IntegerField()
	Estado = models.CharField(max_length=10, default='')

	def __str__(self):
		txt="{0}"
		return txt.format(self.materialess)

class Pedir_Danzas(models.Model):
	codigo=models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='HDanzas')
	material = models.ForeignKey(Inv_Danzas, null=False, blank=False, on_delete=models.CASCADE)
	pedir = models.IntegerField()
	Fecha_Solicitado = models.DateTimeField(default=timezone.now)
	Fecha_a_Pedir = models.DateField(default=timezone.now)
	Fecha_Limite = models.DateField(default=timezone.now)

	def __str__(self):
		txt="El dia {0}. El usuario {1} a pedido {2} {3}, Para el {4} hasta el {5}"
		fech0=self.Fecha_Solicitado.strftime("%A-%d/%B/%Y a las %I:%M %p")
		fech1=self.Fecha_a_Pedir.strftime("%A-%d/%B/%Y")
		fech2=self.Fecha_Limite.strftime("%A-%d/%B/%Y")
		return txt.format(fech0, self.user, self.pedir, self.material, fech1, fech2)


############################################################################################

class Inv_Foto(models.Model):
	codigo=models.AutoField(primary_key=True)
	materialess=models.CharField(max_length=50, default='')
	disponible=models.IntegerField()
	Estado = models.CharField(max_length=10, default='')

	def __str__(self):
		txt="{0}"
		return txt.format(self.materialess)

class Pedir_Foto(models.Model):
	codigo=models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='HFoto')
	material = models.ForeignKey(Inv_Foto, null=False, blank=False, on_delete=models.CASCADE)
	pedir = models.IntegerField()
	Fecha_Solicitado = models.DateTimeField(default=timezone.now)
	Fecha_a_Pedir = models.DateField(default=timezone.now)
	Fecha_Limite = models.DateField(default=timezone.now)

	def __str__(self):
		txt="El dia {0}. El usuario {1} a pedido {2} {3}, Para el {4} hasta el {5}"
		fech0=self.Fecha_Solicitado.strftime("%A-%d/%B/%Y a las %I:%M %p")
		fech1=self.Fecha_a_Pedir.strftime("%A-%d/%B/%Y")
		fech2=self.Fecha_Limite.strftime("%A-%d/%B/%Y")
		return txt.format(fech0, self.user, self.pedir, self.material, fech1, fech2)

