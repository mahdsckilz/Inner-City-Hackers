from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
import os

class City(models.Model):
	name = models.CharField(max_length=200)
	state = models.CharField(max_length=3)
	heading1 = models.TextField(default='')
	para1 = models.TextField(default='')
	heading2 = models.TextField(default='', blank=True)
	para2 = models.TextField(default='', blank=True)
	
	def __unicode__(self):
		return '%s %s' % (self.name)
		
	def __str__(self):
		return '%s' % (self.name)

		
class SearchGroup(models.Model):

	class Meta:
		verbose_name_plural = "Search Groups"

	groupName = models.CharField(max_length=200)

class College(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	email = models.EmailField(default='')
	departments = models.TextField(default='')
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='college/')

class Library(models.Model):
	class Meta:
		verbose_name_plural = "Libraries"
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='library/')

class Industry(models.Model):
	class Meta:
		verbose_name_plural = "Industries"
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='industry/')

class Hotel(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='hotel/')

class Park(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='hotel/')

class Zoo(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='zoo/')

class Museum(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='museum/')
    
class Restaurant(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='restaurant/')
    
class Mall(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='mall/')

class Cafe(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	openingHours = models.CharField(max_length=5, default="00:00")
	closingHours = models.CharField(max_length=5, default="00:00")
	description = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	image = models.ImageField(null=True, upload_to='cafe/')