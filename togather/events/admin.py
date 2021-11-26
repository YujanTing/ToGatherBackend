from django.contrib import admin
from .models import Event
# from .models import User_special

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_type','event_location','event_description')
    pass
admin.site.register(Event, EventAdmin)
# admin.site.register(User_special)