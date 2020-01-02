from rest_framework import serializers
from products.models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','description')

        
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title','category_id','created_at','updated_at')