from django import forms
from inventory.models import UserProfile


class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('city', 'searchGroup')
		