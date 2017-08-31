from django.shortcuts import render
from django.http import Http404

from inventory.models import *

def index(request):
    return render(request, 'inventory/index.html', {
        })
		
def search(request):
		try:
			colleges = College.objects.all()
		except College.DoesNotExist:
			raise Http404('This item does not exist')
		try:
			hotels = Hotel.objects.all()
		except Hotel.DoesNotExist:
			raise Http404('This item does not exist')
		return render(request, 'inventory/search.html', {
        'colleges': colleges,
		'hotels' : hotels,
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