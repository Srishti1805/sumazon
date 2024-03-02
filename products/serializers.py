from .models import Products, Order
from rest_framework import serializers


class JSONSerializerField(serializers.Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    incomingData = JSONSerializerField()

    class Meta:
        model = Order
        fields = "__all__"


class ProductQuantitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
