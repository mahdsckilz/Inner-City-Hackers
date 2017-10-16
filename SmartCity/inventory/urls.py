from django.conf.urls import patterns, include, urls

urlpatterns = patterns('',
	url(r'^profile/$', 'userprofile.views.user_profile'),
)