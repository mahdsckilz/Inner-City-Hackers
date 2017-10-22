from django.db import models
from inventory.models import City, SearchGroup
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	city = models.ForeignKey(City,on_delete=models.CASCADE, null=True)
	searchGroup = models.ForeignKey(SearchGroup,on_delete=models.CASCADE, null=True)
	
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
	
