from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.create, name='create'),
path('delete/<int:id>', views.delete, name='delete'),
]
