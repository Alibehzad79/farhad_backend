from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions, response

from carts_app.models import Cart
from products_app.models import Product
from carts_app.serializers import AddCartSerializer, CartSerializer

# Create your views here.


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def add_cart(request):
    user = request.user
    serializer = AddCartSerializer(data=request.data)
    if serializer.is_valid():
        product = Product.objects.get(slug=serializer.data["product_slug"])
        if Cart.objects.filter(product=product, user=user).exists():
            cart = Cart.objects.get(product=product, user=user)
            cart.quantity = serializer.data["quantity"]
            cart.save()
            return response.Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        else:
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


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_cart_list_api_view(request):
    carts = Cart.objects.filter(user=request.user).all()
    amount = 0
    for cart in carts:
        amount += cart.total_price()

    cart_serializer = CartSerializer(carts, many=True)
    serializer = {"carts": cart_serializer.data, "amount": amount}
    return response.Response(data=serializer, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def edit_cart(request):
    user = request.user
    serializer = AddCartSerializer(data=request.data)
    if serializer.is_valid():
        product = Product.objects.get(slug=serializer.data["product_slug"])
        cart = Cart.objects.get(user=user, product=product)
        cart.quantity = serializer.data["quantity"]
        cart.save()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_cart_api_view(request):
    user = request.user
    cart_id = request.data["cart_id"]
    try:
        cart = Cart.objects.get(user=user, id=cart_id)
        cart.delete()
        return response.Response(
            data={"message": "با موفقیت حذف شد."}, status=status.HTTP_204_NO_CONTENT
        )
    except:
        return response.Response(
            data={"message": "کارت پیدا نشد."}, status=status.HTTP_400_BAD_REQUEST
        )
