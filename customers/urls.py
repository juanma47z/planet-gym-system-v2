from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('add/', views.customer_create, name='customer_create'),
    path('<int:id>/edit/', views.customer_update, name='customer_update'),
    path('<int:id>/delete/', views.customer_delete, name='customer_delete'),
    path('<int:id>/detail/', views.customer_detail, name='customer_detail'),
]