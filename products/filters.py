from .models import Products
import django_filters

class ProductsFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ['price']