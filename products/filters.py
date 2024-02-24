from .models import Products, Order
import django_filters

class ProductsFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ['price']

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['userId']