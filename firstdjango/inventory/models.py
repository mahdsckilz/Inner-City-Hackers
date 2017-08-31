from django.db import models

class College(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    departments = models.TextField(default='')
    
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
