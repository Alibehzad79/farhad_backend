from django.urls import path
from carts_app.views import (
    add_cart,
    get_cart_list_api_view,
    edit_cart,
    delete_cart_api_view,
)

urlpatterns = [
    path("add/", add_cart, name="add_cart"),
    path("list/", get_cart_list_api_view, name="get_cart_list_api_view"),
    path("edit/", edit_cart, name="edit_cart"),
    path("delete/", delete_cart_api_view, name="delete_cart_api_view"),
]
