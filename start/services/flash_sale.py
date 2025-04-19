from rest_framework.decorators import api_view
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from datetime import datetime, timedelta
from start.models import Product, Flashsale, ProductViewHistory


class FlashSaleListCreatView(generics.ListCreateAPIView):
    queryset = Flashsale.objects.all()


    class FlashSaleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Flashsale
            fields = ('id', 'product', 'discount_percentage', 'start_time', 'end_time')

    serializer_class = FlashSaleSerializer

@api_view(['GET'])
def chech_flash_sale(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': "Product not found. "}, status=status.HTTP_404_NOT_FOUND)

    user_viewed = ProductViewHistory.objects.filter(user=request.user, product=product).exists()

    upcoming_flash_sale = Flashsale.objects.filter(
        product=product,
        start_time__lte = datetime.now() + timedelta(hours=24)
    ).first()

    if user_viewed and upcoming_flash_sale:
        discount = upcoming_flash_sale.discount_percentage
        start_time = upcoming_flash_sale.start_time
        end_time = upcoming_flash_sale.end_time
        return Response({ 
            "mesage": f"This product will be on a {discount}% off flash sale!",
            "start_time": start_time,
            "end_time": end_time
        })
    else:
        return Response({
            "message": "No upcoming flash sales for this product"
        })