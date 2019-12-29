from rest_framework import serializers
from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','description')

        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title','category_id','created_at','updated_at')