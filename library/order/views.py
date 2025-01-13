from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from order.models import Order
from book.models import Book
from datetime import timedelta
from django.utils.timezone import now

def create(request):
    if not request.user.is_authenticated:
        return render('401.html')
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book.objects.get(pk=book_id)
        user = request.user
        Order.objects.create(
            book=book,
            user=user,
            plated_end_at=now() + timedelta(weeks=2)
        )
        return redirect('authentication:user_details', user.id)

def delete(request, id):
    try:
        Order.objects.get(pk=id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except Order.DoesNotExist:
        return render(request, '404.html')
