from django.core.exceptions import ValidationError
from start.models import Order

def place_order(product, customer, quantity):
    if product and customer and quantity > 0:
        order = Order(product=product, customer=customer, quantity=quantity)
        order.save()
        return order
    else:
        raise ValidationError('Invalid order parameters.')