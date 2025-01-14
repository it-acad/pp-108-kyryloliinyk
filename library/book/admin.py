from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'count')
    search_fields = ('name', 'description')
    list_filter = ('count', 'authors')

admin.site.register(Book, BookAdmin)

