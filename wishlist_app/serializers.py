from rest_framework import serializers
from wishlist_app.models import Wishlist
from products_app.serializers import ProductSerializer
from products_app.models import Product


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(
        read_only=True,
    )

    class Meta:
        model = Wishlist
        exclude = ("user",)


class ToggleWishlistSerializer(serializers.Serializer):
    product_slug = serializers.SlugField(required=True)

    def validate_product_slug(self, value):
        if not Product.objects.filter(slug=value).exists():
            raise serializers.ValidationError("محصول یافت نشد.")
        return value
