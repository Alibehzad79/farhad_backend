from django.urls import path
from wishlist_app.views import wishlist_api_view

urlpatterns = [
    path(
        "list/",
        wishlist_api_view,
        name="wishlist_api_view",
    ),
]
