from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'author_list')
    search_fields = ('name', 'description')
    list_filter = ('count', 'authors')

    def author_list(self, obj):
        return ", ".join([author.__str__() for author in obj.authors.all()])
    author_list.short_description = 'Authors'

admin.site.register(Book, BookAdmin)
