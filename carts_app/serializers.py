from rest_framework import serializers
from django.core import validators
from products_app.models import Product


class CartSerializer(serializers.Serializer):
    product_slug = serializers.SlugField(required=True)
    quantity = serializers.IntegerField(
        required=True,
        validators=[validators.MinValueValidator(1, "حداقل مقدار باید 1 باشد.")],
    )

    def validate_product_slug(self, value):
        if not Product.objects.filter(slug=value).exists():
            raise serializers.ValidationError("محصولی یافت نشد.")
        return value

    def validate(self, data):
        product_slug = data.get("product_slug")
        quantity = data.get("quantity")
        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise serializers.ValidationError({"product_slug": "محصول یافت نشد."})

        if quantity > product.count:
            raise serializers.ValidationError(
                {"quantity": "مقدار درخواستی بیشتر از مقدار موجود در انبار است."}
            )
        return data
