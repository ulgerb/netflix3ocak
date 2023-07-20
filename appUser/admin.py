from django.contrib import admin
from .models import *




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   '''Admin View for Profile'''

   list_display = ('user','name','loginp','id')

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
   '''Admin View for Profile'''

   list_display = ('user','id')