from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings

COLUMN_SMALL_SIZE = 128

class Batelada(models.Model):
	batelada = models.IntegerField(default=0)
	tanque  = models.IntegerField(default=0)
	OG = models.FloatField(default=0)
	FG = models.FloatField(default=0)
	volume = models.FloatField('volume [L]', default=0)
	data = models.DateTimeField('data da batelada')
	estilo = models.CharField(max_length=COLUMN_SMALL_SIZE)
	cervejeiro = models.CharField(max_length=COLUMN_SMALL_SIZE)
	marca = models.CharField(max_length=COLUMN_SMALL_SIZE)
	obs = models.TextField('observações')
	
	def __str__(self):
		return 'Batelada {0}'.format(self.batelada)
	
	
class Medida(models.Model):
	batelada = models.ForeignKey(Batelada, on_delete=models.CASCADE)
	SG = models.FloatField(default=0)
	data = models.DateTimeField('data da medida')
	pressao = models.FloatField('Pressão [bar]', default=0)
	temeratura = models.FloatField('Temperatura [°C]', default=0)
	obs = models.TextField('observações')
	
	def __str__(self):
		return '{0}: {1}'.format(self.batelada, self.data)
		
class Batelada2(models.Model):
	batelada = models.IntegerField(default=0)
	tanque  = models.IntegerField(default=0)
	OG = models.FloatField(default=0)
	FG = models.FloatField(default=0)
	volume = models.FloatField('volume [L]', default=0)
	data = models.DateTimeField('data da batelada')
	estilo = models.CharField(max_length=COLUMN_SMALL_SIZE)
	cervejeiro = models.CharField(max_length=COLUMN_SMALL_SIZE)
	marca = models.CharField(max_length=COLUMN_SMALL_SIZE)
	obs = models.TextField('observações')
	
	def __str__(self):
		return 'Batelada {0}'.format(self.batelada)
	
	
class Medida2(models.Model):
	batelada = models.ForeignKey(Batelada, on_delete=models.CASCADE)
	SG = models.FloatField(default=0)
	data = models.DateTimeField('data da medida')
	pressao = models.FloatField('Pressão [bar]', default=0)
	temeratura = models.FloatField('Temperatura [°C]', default=0)
	obs = models.TextField('observações')
	
	def __str__(self):
		return '{0}: {1}'.format(self.batelada, self.data)
