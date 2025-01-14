from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')
    list_filter = ('surname',)

admin.site.register(Author, AuthorAdmin)
