from django.contrib import admin
from wishlist_app.models import Wishlist

# Register your models here.


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "date_add")
    list_filter = ("date_add",)
    search_fields = ("user__username", "product__title", "product__slug")
