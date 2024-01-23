from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.item_list, name='items'),
    path('item/<str:pk>/', views.item_edit, name='item'),
    path('create', views.item_create, name='create'),
    path('delete/<str:pk>/', views.item_delete, name='delete'),
    path('completed', views.item_completed, name='completed'),
]