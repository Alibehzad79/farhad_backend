from django.shortcuts import render, redirect
from django.utils.http import urlencode
from rest_framework import response, status, permissions
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse, Http404
import json
from django.contrib.auth.hashers import get_random_string
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken

#######
from orders_app.models import Order, OrderItem
from carts_app.models import Cart
from orders_app.serializers import OrderSerializer

######
import logging
from django.urls import reverse
from azbankgateways import (
    bankfactories,
    models as bank_models,
    default_settings as settings,
)
from azbankgateways.exceptions import AZBankGatewaysException

from config import settings as config_settings


def go_to_gateway_view(request):
    order_id = request.GET.get("order_id")
    token = request.GET.get("token")

    if order_id is None or token is None:
        return HttpResponse(f"ایدی سفارش یافت نشد")
    try:
        access_token = AccessToken(token)  # Decode token
        user_id = access_token["user_id"]  # Extract user ID
        user = get_user_model().objects.get(id=user_id)
    except Exception:
        return HttpResponse("توکن نامعتبر")

    try:
        order = Order.objects.get(order_id=order_id, user=user)
    except Order.DoesNotExist:
        return HttpResponse("سفاری یافت نشد.")
    if order.status == "paid":
        return HttpResponse("سفاری از قبل پرداخت شده است.")
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = order.total_price
    print(amount)
    # user_mobile_number = "+989112221234"  # اختیاری
    query_params = {"order_id": order.order_id, "token": token}
    factory = bankfactories.BankFactory()
    try:
        bank = (
            factory.auto_create()
        )  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url(
            reverse("callback-gateway") + "?" + urlencode(query_params)
        )
        # bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()
        print(bank_record)

        # هدایت کاربر به درگاه بانک
        context = bank.get_gateway()
        return render(request, "redirect_to_bank.html", context=context)
    except AZBankGatewaysException as e:
        logging.critical(e)
        return render(request, "redirect_to_bank.html")


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    order_id = request.GET.get("order_id")
    token = request.GET.get("token")

    if order_id is None or token is None:
        return HttpResponse(f"ایدی سفارش یافت نشد")
    try:
        access_token = AccessToken(token)  # Decode token
        user_id = access_token["user_id"]  # Extract user ID
        user = get_user_model().objects.get(id=user_id)
    except Exception:
        return HttpResponse("توکن نامعتبر")

    try:
        order = Order.objects.get(order_id=order_id, user=user)
    except Order.DoesNotExist:
        return HttpResponse("سفاری یافت نشد.")

    try:
        carts = Cart.objects.filter(user=user).all()
    except:
        return HttpResponse("سبد خرید یافت نشد.")

    if len(carts) < 1:
        return response.Response(
            data={"error": "سبد خرید خالی است."}, status=status.HTTP_400_BAD_REQUEST
        )

    if order.status == "paid":
        return HttpResponse("سفاری از قبل پرداخت شده است.")

    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        order.pay_status = "paid"
        order.status = "pending"
        carts.delete()
        order.save()
        return redirect(
            config_settings.FRONTEND_URL
            + "/accounts/profile/payments/pay-status?status=OK"
        )
    order.pay_status = "cancled"
    order.status = "cancled"
    order.save()
    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return redirect(
        config_settings.FRONTEND_URL
        + "/accounts/profile/payments/pay-status?status=NOK"
    )


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_order(request):
    user = request.user
    data = request.data

    order_id = get_random_string(32)

    carts = Cart.objects.filter(user=user).all()

    if len(carts) < 1:
        return response.Response(
            data={"error": "سبد خرید خالی است."}, status=status.HTTP_400_BAD_REQUEST
        )

    total_price = sum(cart.total_price() for cart in carts)
    user_info = request.data["user_info"]
    new_order = Order.objects.create(
        user=user,
        order_id=order_id,
        date_created=timezone.now(),
        total_price=total_price,
        user_info=f"نام و نام خانوادگی: {user_info['first_name']} {user_info['last_name']} \n\n شماره تماس: {user_info['phone_number']} \n\n ایمیل: {user_info['email']} \n\n آدرس: {user_info['address']}\n\n",
    )
    for cart in carts:
        OrderItem.objects.create(
            order=new_order,
            product=cart.product,
            quantity=cart.quantity,
            price=cart.total_price(),
        )
    if new_order is not None:
        new_order.save()
    return response.Response(
        data={"order_id": new_order.order_id},
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def user_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user).all()
    serializer = OrderSerializer(orders, many=True)
    return response.Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def order_detail(request):
    user = request.user
    try:
        order_id = request.GET["order_id"]
    except:
        return response.Response(
            data={"msg": "سفارش یافت نشد."}, status=status.HTTP_404_NOT_FOUND
        )
    try:
        order = Order.objects.get(user=user, order_id=order_id)
    except:
        return response.Response(
            data={"msg": "سفارش یافت نشد."}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = OrderSerializer(order)
    return response.Response(data=serializer.data, status=status.HTTP_200_OK)
