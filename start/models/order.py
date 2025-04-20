from django.db import models
from .product import Product
from django.core.validators import RegexValidator

from django.contrib.auth import get_user_model
User = get_user_model()

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be in the format: '+998xxxxxxxxx'."
)

class Order(models.Model):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True, null=True)
    is_paid = models.BooleanField(default=False, null=True)

    def set_status(self, new_status):
        allowed_transitions = {
            self.PENDING: [self.PROCESSING, self.CANCELLED],
            self.PROCESSING: [self.SHIPPED, self.CANCELLED],
            self.SHIPPED: [self.DELIVERED, self.CANCELLED],
        }

        return new_status in allowed_transitions.get(self.status, [])

    def __str__(self):
        return f"Order({self.product.name} by {self.customer.name})"