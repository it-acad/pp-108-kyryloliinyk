from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('details/<int:id>', views.details, name='details'),
path('search/', views.search, name='search'),
]
