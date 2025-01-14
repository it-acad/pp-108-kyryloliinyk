from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_list', 'count')
    search_fields = ('name', 'description')
    list_filter = ('count', 'authors')

    # Mark `name` and `author_list` as read-only fields
    readonly_fields = ('name', 'author_list')

    def author_list(self, obj):
        return ", ".join([str(author) for author in obj.authors.all()])
    author_list.short_description = 'Authors'

    fieldsets = (
        ('Immutable Data', {  # Section for data that doesn't change
            'fields': ('name', 'author_list')  # Both are read-only
        }),
        ('Mutable Data', {  # Section for data that changes
            'fields': ('count',)
        }),
    )

admin.site.register(Book, BookAdmin)
