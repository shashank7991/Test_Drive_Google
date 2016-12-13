from django.contrib import admin

# Register your models here.
from .models import Users, Trips, Events, Role #this line added

class u_class(admin.ModelAdmin):
    list_display = ["user_id"]

admin.site.register(Users)#this line added
admin.site.register(Trips)#this line added
admin.site.register(Events)#this line added
admin.site.register(Role)#this line added