from django.conf.urls import url
from django.contrib import admin

from inventory import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^bootstrap', views.bootstrap, name='bootstrap'),
	url(r'^search', views.search, name='search'),
    url(r'^college/(?P<id>\d+)/', views.college_detail, name='college'),
    url(r'^library/(?P<id>\d+)/', views.library_detail, name='library'),
    url(r'^industry/(?P<id>\d+)/', views.industry_detail, name='industry'),
    url(r'^hotel/(?P<id>\d+)/', views.hotel_detail, name='hotel'),
    url(r'^park/(?P<id>\d+)/', views.park_detail, name='park'),
    url(r'^zoo/(?P<id>\d+)/', views.zoo_detail, name='zoo'),
    url(r'^museum/(?P<id>\d+)/', views.museum_detail, name='museum'),
    url(r'^restaurant/(?P<id>\d+)/', views.restaurant_detail, name='restaurant'),
    url(r'^mall/(?P<id>\d+)/', views.mall_detail, name='mall'),    
	url(r'^cafe/(?P<id>\d+)/', views.cafe_detail, name='cafe'),    
    url(r'^admin/', admin.site.urls),
]