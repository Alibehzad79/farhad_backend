from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products_app.models import Category, Tag, Product
from products_app.serializers import (
    ProductSerializer,
    CategorySerializer,
    TagSerializer,
)

# Create your views here.


@api_view(["GET"])
def product_list_api_view(request):
    products = Product.objects.order_by("-date_created").all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def product_detail_api_view(request, *args, **kwargs):
    try:
        product = Product.objects.get(id=kwargs["id"])
    except:
        raise Response(
            data={"message": "محصولی یافت نشد."}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def categories_api_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def tags_api_view(request):
    tags = Category.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

