from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, get_random_string
from django.core.mail import send_mail
from accounts_app.serializers import RegisterSerializer, ResetPasswordSerializer
from config import settings

# Create your views here.


@api_view(["POST"])
def register_api_view(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            new_user = get_user_model().objects.create(
                username=request.data["email"].lower(),
                email=request.data["email"].lower(),
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                password=make_password(request.data["password"]),
            )
            if new_user is not None:
                new_user.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def send_reset_password_email_api_view(request):
    serializer = ResetPasswordSerializer(data=request.data)
    if serializer.is_valid():
        user = get_user_model().objects.get(email=serializer.data["email"])
        token = get_random_string(32)
        user.reset_password_token = token
        user.save()
        try:
            send_mail(
                subject="بازیابی رمز عبور",
                message=f"{settings.FRONTEND_URL}/accounts/forgot-password/token-{user.reset_password_token}/",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[serializer.data["email"]],
            )
            return Response(
                data={"message": "ایمیل با موفقیت ارسال شد."}, status=status.HTTP_200_OK
            )
        except:
            return Response(
                data={"message": "خطا در ارسال ایمیل"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
