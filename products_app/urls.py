from django.urls import path

from products_app.views import (
    product_detail_api_view,
    product_list_api_view,
    categories_tags_api_view,
    # tags_api_view,
    product_list_by_search_api_view,
)

urlpatterns = [
    path(
        "",
        product_list_api_view,
        name="product_list_api_view",
    ),
    path(
        "detail/<slug:slug>/",
        product_detail_api_view,
        name="product_detail_api_view",
    ),
    path(
        "categories_tags/",
        categories_tags_api_view,
        name="categories_api_view",
    ),
    # path(
    #     "tags/",
    #     tags_api_view,
    #     name="tags_api_view",
    # ),
    path(
        "search/",
        product_list_by_search_api_view,
        name="product_list_by_search_api_view",
    ),
]
