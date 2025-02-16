from django.urls import path
from wishlist_app.views import wishlist_api_view, toggle_wishlist_api_view

urlpatterns = [
    path(
        "list/",
        wishlist_api_view,
        name="wishlist_api_view",
    ),
    path(
        "toggle/",
        toggle_wishlist_api_view,
        name="toggle_wishlist_api_view",
    ),
]
