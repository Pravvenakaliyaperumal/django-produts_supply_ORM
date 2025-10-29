from django.shortcuts import render, redirect
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



# ---------------------- ADD FORMS ------------------------
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('description')
        Category.objects.create(name=name, description=desc)
        return redirect('view_categories')
    return render(request, 'products/add_category.html')


def add_supplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        Supplier.objects.create(name=name, email=email, phone_number=phone_number)
        return redirect('view_suppliers')
    return render(request, 'products/add_supplier.html')


def add_product(request):
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        supplier_id = request.POST.get('supplier')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        Product.objects.create(
            name=name,
            category_id=category_id,
            supplier_id=supplier_id,
            price=price,
            stock=stock
        )
        return redirect('view_products')
    return render(request, 'products/add_product.html', {
        'categories': categories,
        'suppliers': suppliers
    })