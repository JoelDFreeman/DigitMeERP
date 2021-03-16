from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('products/', views.Products),
    path('orders/', views.Orders),
    path('companies/', views.Companies),
]