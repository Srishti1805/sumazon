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
        return models.Order.objects.filter(userId=self.request.user)

    def create(self, request):
        data = request.data
        serializer = serializers.ProductQuantitySerializer(data=data, many=True)
        products = []
        if serializer.is_valid():
            for item in serializer.validated_data:
                product_id = item["id"]
                quantity = item["quantity"]
                try:
                    product = models.Products.objects.get(id=product_id)
                except models.Products.DoesNotExist:
                    return Response(
                        f"Product with id {product_id} does not exist.",
                        status=status.HTTP_404_NOT_FOUND,
                    )
                if quantity > product.quantity:
                    return Response(
                        f"Quantity for product {product.name} is greater than current stock.",
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                product.quantity -= quantity
                products.append(product)
            models.Products.objects.bulk_update(products, ["quantity"])

            serializer = serializers.OrderSerializer(
                data={"incomingData": data, "userId": request.user.id}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    "Product quantities updated successfully.",
                    status=status.HTTP_200_OK,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        return Response("METHOD NOT ALLOWED", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        return Response("METHOD NOT ALLOWED", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return Response("METHOD NOT ALLOWED", status=status.HTTP_405_METHOD_NOT_ALLOWED)
