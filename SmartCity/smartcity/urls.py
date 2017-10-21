from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from smartcity import views as smartcityviews
from inventory import views as inventoryviews
from userprofile import views as userprofileviews

urlpatterns = [	

	url(r'^accounts/login/$', smartcityviews.login),
	url(r'^accounts/auth/$', smartcityviews.auth_view),	
	url(r'^accounts/loggedin/$', smartcityviews.loggedin),
	url(r'^accounts/invalid/$', smartcityviews.invalid_login),
	url(r'^accounts/register/$', userprofileviews.register_user),
	url(r'^accounts/register_success/$', smartcityviews.register_success),
	
	url(r'^$', inventoryviews.index, name='index'),
	url(r'^bootstrap', inventoryviews.bootstrap, name='bootstrap'),
	url(r'^search', inventoryviews.search, name='search'),
    url(r'^college/(?P<id>\d+)/', inventoryviews.college_detail, name='college'),
    url(r'^library/(?P<id>\d+)/', inventoryviews.library_detail, name='library'),
    url(r'^industry/(?P<id>\d+)/', inventoryviews.industry_detail, name='industry'),
    url(r'^hotel/(?P<id>\d+)/', inventoryviews.hotel_detail, name='hotel'),
    url(r'^park/(?P<id>\d+)/', inventoryviews.park_detail, name='park'),
    url(r'^zoo/(?P<id>\d+)/', inventoryviews.zoo_detail, name='zoo'),
    url(r'^museum/(?P<id>\d+)/', inventoryviews.museum_detail, name='museum'),
    url(r'^restaurant/(?P<id>\d+)/', inventoryviews.restaurant_detail, name='restaurant'),
    url(r'^mall/(?P<id>\d+)/', inventoryviews.mall_detail, name='mall'),    
	url(r'^cafe/(?P<id>\d+)/', inventoryviews.cafe_detail, name='cafe'), 
    url(r'^admin/', admin.site.urls),
	]
	
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)