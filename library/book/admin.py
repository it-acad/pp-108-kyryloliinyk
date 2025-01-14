from django.contrib import admin
from .models import Book

class DistinctListFilter(admin.SimpleListFilter):
    title = 'Publication Year'
    parameter_name = 'publication_year'

    def lookups(self, request, model_admin):
        unique_years = Book.objects.order_by('publication_year').values_list('publication_year', flat=True).distinct()
        return [(year, year) for year in unique_years if year is not None]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(publication_year=self.value())
        return queryset


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_list', 'count', 'publication_year')
    search_fields = ('name', 'description')
    list_filter = ('count', DistinctListFilter)

    def author_list(self, obj):
        return ", ".join([str(author) for author in obj.authors.all()])
    author_list.short_description = 'Authors'

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Edit form
            return ('name', 'author_list', 'publication_year')
        return ()

    def get_fieldsets(self, request, obj=None):
        if obj:  # Edit form
            return (
                ('Immutable Data', {
                    'fields': ('name', 'author_list', 'publication_year'),
                }),
                ('Mutable Data', {
                    'fields': ('description', 'count', 'last_issued_date'),
                }),
            )
        else:  # Create form
            return (
                ('Create Book', {
                    'fields': ('name', 'description', 'count', 'publication_year'),
                }),
            )

admin.site.register(Book, BookAdmin)
