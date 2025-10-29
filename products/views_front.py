from django.shortcuts import render
from .models import Product, Category, Supplier

def home(request):
    return render(request, 'home.html')

def view_products(request):
    products = Product.objects.select_related('category', 'supplier')
    return render(request, 'products/view_products.html', {'products': products})

def view_categories(request):
    categories = Category.objects.all()
    return render(request, 'products/view_categories.html', {'categories': categories})

def view_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'products/view_suppliers.html', {'suppliers': suppliers})
