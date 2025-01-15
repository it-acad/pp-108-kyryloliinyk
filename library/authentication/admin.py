from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')
    search_fields = ('email', 'first_name', 'last_name', 'email')
    list_filter = ('role','is_staff', 'is_superuser')

admin.site.register(CustomUser, CustomUserAdmin)
