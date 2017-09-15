from django.db import models

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


class College(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200, default='')
	email = models.EmailField(default='')
	departments = models.TextField(default='')
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)

	

class Library(models.Model):
    class Meta:
        verbose_name_plural = "Libraries"
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()

class Industry(models.Model):
    class Meta:
        verbose_name_plural = "Industries"
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()

class Hotel(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()

class Park(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()

class Zoo(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()

class Museum(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()
    
class Restaurant(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()
    
class Mall(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()

class Cafe(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    openingHours = models.CharField(max_length=5, default="00:00")
    closingHours = models.CharField(max_length=5, default="00:00")
    description = models.TextField()