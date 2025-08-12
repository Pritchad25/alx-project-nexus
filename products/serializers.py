from rest_framework import serializers
from .models import Product
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        model = Product
        fields = '__all__'
