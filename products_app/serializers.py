from rest_framework import serializers
from products_app.models import Category, Tag, Product
from config import settings


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    image = serializers.SerializerMethodField()
    galleries = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    discount_price = serializers.FloatField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_image(self, obj):
        return f"{settings.BACKEND_URL}{obj.image.url}"

    def get_discount_price(self, obj):
        return self.get_discount_price()

    def get_galleries(self, obj):
        return (
            {
                "title": gallery.title,
                "image": f"{settings.BACKEND_URL}{gallery.image.url}",
            }
            for gallery in obj.galleries.all()
        )

    def get_options(self, obj):
        return (
            {
                "title": option.title,
                "description": option.description,
            }
            for option in obj.options.all()
        )
