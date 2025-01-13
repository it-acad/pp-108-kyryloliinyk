from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('authenticate/', views.authenticate, name='authenticate'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('logout/<int:id>', views.logout, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:id>', views.user_details, name='user_details'),
]
