from django.urls import path
from orders_app.views import (
    create_order,
    user_orders,
    order_detail,
    go_to_gateway_view,
    callback_gateway_view,
)

urlpatterns = [
    path(
        "create/",
        create_order,
        name="create_order",
    ),
    path(
        "list/",
        user_orders,
        name="user_orders",
    ),
    path(
        "detail/",
        order_detail,
        name="order_detail",
    ),
    path(
        "request/",
        go_to_gateway_view,
        name="go_to_gateway_view",
    ),
    path(
        "callback-gateway/",
        callback_gateway_view,
        name="callback-gateway",
    ),
]
