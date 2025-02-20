from django.urls import path
from orders_app.views import (
    create_order,
    # pay_method,
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
