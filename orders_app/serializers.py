from rest_framework import serializers
from orders_app.models import Order, OrderItem
from products_app.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    orderitems = serializers.SerializerMethodField()

    class Meta:
        model = Order
        exclude = ("user",)

    def get_orderitems(self, obj):
        return OrderItemSerializer(obj.orderitems.all(), many=True).data
