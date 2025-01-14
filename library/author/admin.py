from django.contrib import admin
from django.db.models import Count
from .models import Author

# Custom filter for books count
class BooksCountFilter(admin.SimpleListFilter):
    title = 'Books Count'
    parameter_name = 'books_count'

    def lookups(self, request, model_admin):
        return [
            ('0', 'No books'),
            ('1-2', '1 to 2 books'),
            ('3-5', '3 to 5 books'),
            ('6+', 'More than 5 books'),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == '0':
            return queryset.filter(books__isnull=True)  # No related books
        elif value == '1-2':
            return queryset.annotate(book_count=Count('books')).filter(book_count__range=(1, 2))
        elif value == '3-5':
            return queryset.annotate(book_count=Count('books')).filter(book_count__range=(3, 5))
        elif value == '6+':
            return queryset.annotate(book_count=Count('books')).filter(book_count__gt=5)
        return queryset

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'book_count')
    search_fields = ('name', 'surname')
    list_filter = (BooksCountFilter,)

    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

admin.site.register(Author, AuthorAdmin)
