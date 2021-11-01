from .models import *
from django.contrib import admin 
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin 


class CustomTrash(admin.ModelAdmin):
    list_display = ('name', 'description')
class CustomRoom(admin.ModelAdmin):
    list_display = ('name', 'description')

# Register your models here.
admin.site.register(Trash, CustomTrash)
admin.site.register(Room, CustomRoom)