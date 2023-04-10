from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Añadir caracteristica al panel administrador del usuario. 
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        # (None, {'fields': ('username', 'password')}),
        # (None, {'fields': ('username', 'password')}),
        # ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
        # ('Otros', {'fields': ('is_activate', )}),
    )

