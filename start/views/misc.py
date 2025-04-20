from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from start.models import Order, Category, Review
from start.permissions import IsOwnerOrReadOnly
from start.serializers import OrderSerializer, ReviewSerializer, CategorySerializer

class OrderViewset(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
