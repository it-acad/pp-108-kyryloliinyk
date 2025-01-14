from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')
    search_fields = ('email', 'first_name', 'last_name', 'email')
    list_filter = ('role',)

admin.site.register(CustomUser, CustomUserAdmin)
