from django.urls import path

from products_app.views import (
    product_detail_api_view,
    product_list_api_view,
    categories_api_view,
    tags_api_view,
)

urlpatterns = [
    path(
        "",
        product_list_api_view,
        name="product_list_api_view",
    ),
    path(
        "categories/",
        categories_api_view,
        name="categories_api_view",
    ),
    path(
        "tags/",
        tags_api_view,
        name="tags_api_view",
    ),
]
