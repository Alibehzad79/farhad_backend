from django.shortcuts import render
from rest_framework import response, status, permissions
from rest_framework.decorators import api_view, permission_classes

from wishlist_app.models import Wishlist
from wishlist_app.serializers import WishlistSerializer

# Create your views here.


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def wishlist_api_view(request):
    user = request.user
    wishlist = Wishlist.objects.filter(user=user).all().distinct()
    serializer = WishlistSerializer(wishlist, many=True)
    return response.Response(data=serializer.data, status=status.HTTP_200_OK)
