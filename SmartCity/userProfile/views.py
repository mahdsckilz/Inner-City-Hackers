from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from userprofile.forms import UserProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from inventory.models import City
from django.contrib import auth

def register_user(request):
	registered = False

	if request.method == 'POST':
		userForm = UserForm(request.POST)
		profileForm = UserProfileForm(request.POST)
		
		if userForm.is_valid():
			user = userForm.save()
			
			user.set_password(user.password)
			user.save()
			
			profile = profileForm.save(commit=False)
			profile.user = user
			
			profile.save()
			
			registered = True
			auth.login(request, user)
			
			return HttpResponseRedirect('/search/', )
		
		else:
			return render_to_response('inventory/index.html')
	
	else:
		userForm = UserForm()
		profileForm = UserProfileForm()
	
	return render_to_response('inventory/search.html')
	
	
	
	
	