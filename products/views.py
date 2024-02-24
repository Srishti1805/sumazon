from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from . import models, serializers, filters
from rest_framework.views import Response
from rest_framework import status

# Create your views here.

class ProductsView(ReadOnlyModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    filterset_class = filters.ProductsFilter
    search_fields = ("name",)
    ordering = ("-id",)


class OrderView(ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filterset_class = filters.OrderFilter
    ordering = ("-id",)


    def get_queryset(self):
        return models.Order.objects.filter(userId = self.request.user)
    
    def create(self, request):
        pass

    def update(self, request, pk=None):
        return Response("METHOD NOT ALLOWED", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        return Response("METHOD NOT ALLOWED", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return Response("METHOD NOT ALLOWED", status=status.HTTP_405_METHOD_NOT_ALLOWED)