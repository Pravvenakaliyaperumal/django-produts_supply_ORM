📘 README.md — Product Inventory Manager (Django + MySQL + REST API)
🧩 Overview

Product Inventory Manager is a simple full-stack Django web application designed to manage products, categories, and suppliers.
It demonstrates a clean modular backend with Django REST Framework (DRF) and a minimal HTML frontend that directly reflects data stored in a MySQL database.

The goal is to provide a professional, extensible base for building internal inventory or admin-panel style applications — complete with CRUD operations, API endpoints, and live database integration.

⚙️ Tech Stack
Layer	Technology	Purpose
Backend	Django 5 + Django REST Framework	Core app & REST API
Database	MySQL	Persistent data storage
Frontend	Django Templates (HTML + Bootstrap optional)	Simple UI for viewing & adding data
API Client	Postman / DRF UI	Testing CRUD endpoints
Hosting (later)	Render / Railway / Azure App Service	Cloud deployment
🗂️ Project Structure
product_api/
│
├── products/
│   ├── templates/
│   │   └── products/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── view_products.html
│   │       ├── view_categories.html
│   │       ├── view_suppliers.html
│   │       ├── add_product.html
│   │       ├── add_category.html
│   │       └── add_supplier.html
│   ├── views_front.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── urls_front.py
│
├── inventoryproject/ (or product_api/)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3 / (MySQL in production)
├── manage.py
└── requirements.txt

🧠 Core Features

✅ 1. REST API with CRUD Endpoints

/api/products/ – Manage products

/api/categories/ – Manage categories

/api/suppliers/ – Manage suppliers

✅ 2. MySQL Database Integration

Data stored and retrieved live from MySQL.

Every insert, update, or delete via frontend / API immediately reflects in the DB.

✅ 3. Frontend Tabs with Dynamic Data

/products/ → Displays product table

/categories/ → Displays category list

/suppliers/ → Displays supplier list

Each page has an “Add New” button for inline data entry.

✅ 4. API Testing with Postman / DRF UI

Endpoints can be tested using raw JSON.

Works seamlessly with JWT auth (can be added later).

✅ 5. Extensible Design

Modular views & serializers make it easy to add authentication, pagination, filtering, or a React frontend later.

🚀 Setup Instructions
1️⃣ Clone & Create Virtual Environment
git clone https://github.com/<username>/product_api.git
cd product_api
python3 -m venv venv
source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Database (settings.py)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4️⃣ Migrate Tables
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Server
python manage.py runserver


➡ Visit http://127.0.0.1:8000

🧪 API Endpoints (for Postman Testing)
Method	Endpoint	Description
GET	/api/products/	List all products
POST	/api/products/	Add new product
GET	/api/categories/	List all categories
POST	/api/categories/	Add new category
GET	/api/suppliers/	List all suppliers
POST	/api/suppliers/	Add new supplier

Example POST payload:

{
  "name": "Herbal Shampoo",
  "category": 2,
  "supplier": 1,
  "price": 19.99,
  "stock": 30
}

💾 Frontend Pages
Page	URL	Action
🏠 Home	/	Landing page
📦 Products	/products/	View + Add Products
🧴 Categories	/categories/	View + Add Categories
🧍 Suppliers	/suppliers/	View + Add Suppliers
🌱 Sample Data Seeder (Optional)
python manage.py shell

from products.models import Category, Supplier, Product
from random import randint, choice

Category.objects.bulk_create([
    Category(name='Skincare', description='Lotions and creams'),
    Category(name='Makeup', description='Cosmetics and beauty'),
])

Supplier.objects.bulk_create([
    Supplier(name='GlowPro', email='contact@glowpro.com'),
    Supplier(name='BeautyMart', email='sales@beautymart.com'),
])

categories = list(Category.objects.all())
suppliers = list(Supplier.objects.all())

for i in range(1, 6):
    Product.objects.create(
        name=f'Product {i}',
        category=choice(categories),
        supplier=choice(suppliers),
        price=randint(10, 100),
        stock=randint(5, 50),
    )

🧩 Next Enhancements (Future Roadmap)

🔐 JWT Authentication (using djangorestframework-simplejwt)

🔍 Filtering & Pagination (via django-filter)

⚙️ React / Bootstrap Frontend

☁️ Deployment on Render / Railway (with PostgreSQL)

📊 Admin Dashboard / Analytics Charts

👩‍💻 Author

Praveena Kaliyaperumal
