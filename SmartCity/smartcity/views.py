from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login-tab.html', c)
	
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/search/')
	else:
		return HttpResponseRedirect("/")
		
def loggedin(request):
	return render_to_response('inventory/search.html', {'full_name': request.user})
	
def invalid_login(request):
	return render_to_response('invalid_login.html')

def register_success(request):
	return render_to_response('index.html')