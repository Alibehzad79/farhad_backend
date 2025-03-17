from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import response, status

from site_settings_app.models import Setting, About
from site_settings_app.serializers import (
    SettingSerializer,
    AboutSerializer,
    ContactSerializer,
)
from django.utils import timezone

# Create your views here.


@api_view(["GET"])
def settings_api_view(request):
    try:
        settings = Setting.objects.last()
    except:
        return None

    serializer = SettingSerializer(
        settings,
        many=False,
    )
    return response.Response(
        data=serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def about_api_view(request):
    try:
        about = About.objects.last()
    except:
        return None

    serializer = AboutSerializer(
        about,
        many=False,
    )
    return response.Response(
        data=serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def contact_api_view(request):
    data = request.data
    date_created = timezone.now()
    data["date_created"] = date_created
    serializer = ContactSerializer(data=data, many=False)
    if serializer.is_valid():

        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
