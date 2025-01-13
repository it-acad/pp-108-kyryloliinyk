from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as auth_logout
from authentication.models import CustomUser
from author.models import Author
from order.models import Order

def user_list(request):
    users = CustomUser.objects.filter(role=1)
    return render(request, 'authentication/user/list.html', {'users': users})

def user_details(request, id):
    try:
        user = CustomUser.objects.get(pk=id)
        if user.role == 0:
            orders = Order.objects.filter(user=user).prefetch_related('book')
            authors = None
            users = None
        else:
            orders = Order.objects.prefetch_related('book')
            authors = Author.objects.all()
            users = CustomUser.objects.all()
    except CustomUser.DoesNotExist:
        return render(request, '404.html', status=404)

    has_orders = orders.exists()
    context = {
        'user': user,
        'orders': orders,
        'authors': authors,
        'users': users,
        'has_orders': has_orders,
    }
    return render(request, 'authentication/user/details.html', context)

def authenticate(request):
    return render(request, 'authentication/authenticate.html')

def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        user = CustomUser(first_name = first_name,
                          last_name = last_name,
                          middle_name = middle_name,
                          email = email,
                          password = password,
                          is_active = True,
                          role = 0 if role == 'guest' else 1)
        user.save()
        login(request, user)
        return redirect('authentication:user_details', user.id)
    return render(request, 'authentication/authenticate.html')

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(email=email, password=password)
            user.is_active = True
            user.save()
        except CustomUser.DoesNotExist:
            return render(request, '401.html', status=401)
    login(request, user)
    return redirect('authentication:user_details', user.id)


def logout(request, id):
    user = CustomUser.objects.get(pk=id)
    user.is_active = False
    user.save()
    auth_logout(request)
    return redirect('home')