from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from itertools import chain
from inventory.models import *
from django.contrib.auth.models import User, Group

def index(request):
	city = City.objects.all()
	searchGroup = SearchGroup.objects.all()
	
	request.session.set_test_cookie()

	return render(request, 'inventory/index.html', {
	'city' : city,
	'searchGroup' : searchGroup
})
		
def bootstrap(request):
	request.session.set_test_cookie()
	
	return render(request, 'bootstrap/index.html', {
	})
	
def search(request):

		cityid = request.user.profile.city_id
		city = City.objects.get(id = cityid)
		
		searchGroupid = request.user.profile.searchGroup_id
		searchGroup = SearchGroup.objects.get(id = searchGroupid)
				
		students = User.objects.all()		
		colleges = College.objects.filter(city__name__exact=city.name)
		hotels = Hotel.objects.all()
		industries = Industry.objects.all()
		libraries = Library.objects.all()
		malls = Mall.objects.all()
		museums = Museum.objects.all()
		parks = Park.objects.all()
		restaurants = Restaurant.objects.all()
		zoos = Zoo.objects.all()
		cafes = Cafe.objects.all()
		
		
		return render(request, 'inventory/search.html', {
        'colleges': colleges,
		'hotels' : hotels,
		'industries' : industries,
		'libraries' : libraries,
		'malls' : malls,
		'museums' : museums,
		'parks' : parks,
		'restaurants' : restaurants,
		'zoos' : zoos,
		'students': students,
		'cafes' : cafes,
		'city' : city,
		'searchGroup' : searchGroup,
		})

def college_detail(request, id):
    try:
        item = College.objects.get(id=id)
    except College.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })

def library_detail(request, id):
    try:
        item = Library.objects.get(id=id)
    except Library.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
        
def industry_detail(request, id):
    try:
        item = Industry.objects.get(id=id)
    except Industry.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })

def hotel_detail(request, id):
    try:
        item = Hotel.objects.get(id=id)
    except Hotel.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })

def park_detail(request, id):
    try:
        item = Park.objects.get(id=id)
    except Park.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })    
    
def zoo_detail(request, id):
    try:
        item = Zoo.objects.get(id=id)
    except Zoo.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })

def museum_detail(request, id):
    try:
        item = Museum.objects.get(id=id)
    except Museum.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })

def restaurant_detail(request, id):
    try:
        item = Restaurant.objects.get(id=id)
    except Restaurant.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
 
def mall_detail(request, id):
    try:
        item = Mall.objects.get(id=id)
    except Mall.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
	
def cafe_detail(request, id):
    try:
        item = Cafe.objects.get(id=id)
    except Cafe.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
	
def group_cookie_handler(request, response, groupPOST):
	group = groupPOST
	
	response.set_cookie('group', group)
	

def test(request):
	return render(request, 'inventory/test.html', {
	})

	