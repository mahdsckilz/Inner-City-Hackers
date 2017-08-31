from django.contrib import admin

from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']

admin.site.register(College, ItemAdmin)
admin.site.register(Library, ItemAdmin)
admin.site.register(Industry, ItemAdmin)
admin.site.register(Hotel, ItemAdmin)
admin.site.register(Park, ItemAdmin)
admin.site.register(Zoo, ItemAdmin)
admin.site.register(Museum, ItemAdmin)
admin.site.register(Restaurant, ItemAdmin)
admin.site.register(Mall, ItemAdmin)