from django.urls import path
from carts_app.views import add_cart

urlpatterns = [
    path("add/", add_cart, name="add_cart"),
]
