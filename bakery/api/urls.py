from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', product, name='product'),
    path('products/<int:pk>/sell', sell, name='product'),
    path('products/<int:pk>/restock', restock, name='product'),
    path('orders/', orders, name='orders'),
    path('orders/<int:pk>/', order, name='order'),
    
]