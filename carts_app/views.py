from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions, response

from carts_app.models import Cart
from products_app.models import Product
from carts_app.serializers import CartSerializer

# Create your views here.


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def add_cart(request):
    user = request.user
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        product = Product.objects.get(slug=serializer.data["product_slug"])
        new_cart = Cart.objects.create(
            user=user,
            product=product,
            quantity=serializer.data["quantity"],
        )
        if new_cart is not None:
            new_cart.save()
            return response.Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
