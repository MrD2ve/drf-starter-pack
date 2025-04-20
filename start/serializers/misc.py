from rest_framework import serializers
from django.db import models
from start.models import Product, Review, ProductViewHistory, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)
    price = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'avg_rating']


class ProductViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViewHistory
        fields = '__all__'