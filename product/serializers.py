from rest_framework import serializers
from .models import Brand,Category,Product

class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields="__all__"

class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"