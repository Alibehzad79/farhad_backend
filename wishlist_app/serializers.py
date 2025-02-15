from rest_framework import serializers
from wishlist_app.models import Wishlist
from products_app.serializers import ProductSerializer


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(
        read_only=True,
    )

    class Meta:
        model = Wishlist
        exclude = ("user",)
