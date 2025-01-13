from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from author.models import Author


def list(request):
    authors = Author.objects.all()
    return render(request, 'author/list.html', {'authors': authors})

def details(request, id):
    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        return render(request, '404.html')
    return render(request, 'author/details.html', {'author': author})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def delete(request, id):
    try:
        Author.objects.get(pk=id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except Author.DoesNotExist:
        return render(request, '404.html')