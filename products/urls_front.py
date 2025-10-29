from django.urls import path
from . import views_front

urlpatterns = [
    path('', views_front.home, name='home'),
    path('products/', views_front.view_products, name='view_products'),
    path('categories/', views_front.view_categories, name='view_categories'),
    path('suppliers/', views_front.view_suppliers, name='view_suppliers'),
]
