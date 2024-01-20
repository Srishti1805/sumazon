from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from . import models, serializers, filters

# Create your views here.

class ProductsView(ReadOnlyModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    filterset_class = filters.ProductsFilter
    search_fields = ("name",)
    ordering = ("-id",)
