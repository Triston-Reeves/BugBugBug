from django.contrib import admin
from TownSquare.models import MyUser, Ticket 
from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser, UserAdmin)
admin.site.register(Ticket)
