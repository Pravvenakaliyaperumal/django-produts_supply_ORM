from rest_framework import serializers
from .models import Category, Supplier, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'      

class ProductSerializer(serializers.ModelSerializer):
    Category = CategorySerializer(read_only=True)
    Supplier = SupplierSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'