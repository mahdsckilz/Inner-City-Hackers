from django.contrib import admin

from .models import *

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'city', 'searchGroup']

class SearchGroupAdmin(admin.ModelAdmin):
	list_display = ['groupName']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
	
class CityAdmin(admin.ModelAdmin):
	list_display = ['name', 'state']

admin.site.register(College, ItemAdmin)
admin.site.register(Library, ItemAdmin)
admin.site.register(Industry, ItemAdmin)
admin.site.register(Hotel, ItemAdmin)
admin.site.register(Park, ItemAdmin)
admin.site.register(Zoo, ItemAdmin)
admin.site.register(Museum, ItemAdmin)
admin.site.register(Restaurant, ItemAdmin)
admin.site.register(Mall, ItemAdmin)
admin.site.register(Cafe, ItemAdmin)
admin.site.register(SearchGroup, SearchGroupAdmin)

admin.site.register(City, CityAdmin)

admin.site.register(UserProfile, UserProfileAdmin)