from django.contrib import admin
from .models import Todolist, Place, AppUser
# Register your models here.
admin.site.register(Todolist)
admin.site.register(Place)
admin.site.register(AppUser)