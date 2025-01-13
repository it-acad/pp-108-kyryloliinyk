from django.shortcuts import render, redirect
from book.models import Book
from author.models import Author


def list(request):
    books = Book.objects.all().prefetch_related('authors')
    authors = [book.authors.all() for book in books]
    flattened_authors = [author for book_authors in authors for author in book_authors]
    return render(request, 'book/list.html', {'books': books, 'authors': flattened_authors})

def details(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return render(request, '404.html')
    return render(request, 'book/details.html', {'book': book})

def search(request):
    if request.method == 'POST':
        author_id = request.POST.get('author')
        if author_id:
            books = Book.objects.filter(authors__id=author_id).distinct()
        else:
            books = Book.objects.all()
        authors = Author.objects.all()
        return render(request, 'book/list.html', {'books': books, 'authors': authors})
    return redirect('book:list')
