from django.contrib import admin
from carts_app.models import Cart

# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "quantity",
        "total_price",
    )
    list_editable = ("quantity",)
    search_fields = (
        "product__title",
        "product__slug",
        "user__username",
    )