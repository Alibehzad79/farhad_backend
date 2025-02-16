from django.shortcuts import render
from rest_framework import response, status, permissions
from rest_framework.decorators import api_view, permission_classes
from django.utils import timezone

from wishlist_app.models import Wishlist
from wishlist_app.serializers import WishlistSerializer, ToggleWishlistSerializer
from products_app.models import Product

# Create your views here.


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def wishlist_api_view(request):
    user = request.user
    wishlist = Wishlist.objects.filter(user=user).all().distinct()
    serializer = WishlistSerializer(wishlist, many=True)
    return response.Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def toggle_wishlist_api_view(request):
    user = request.user
    serializer = ToggleWishlistSerializer(data=request.data)
    if serializer.is_valid():
        product = Product.objects.get(slug=serializer.data["product_slug"])

        if Wishlist.objects.filter(product=product, user=user).exists():
            wish = Wishlist.objects.get(product=product, user=user)
            wish.delete()
            return response.Response(
                data={"message": "با موفقیت حذف شد."}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            Wishlist.objects.create(product=product, user=user, date_add=timezone.now())
            return response.Response(
                data={"message": "با موفقیت اضافه شد."}, status=status.HTTP_200_OK
            )
    else:
        return response.Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
