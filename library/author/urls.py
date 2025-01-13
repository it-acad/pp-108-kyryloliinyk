from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('details/<int:id>', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
]
