from django.contrib import admin
from orders_app.models import Order, OrderItem

# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "order_id", "date_created", "status", "pay_status")
    list_display_links = ("user", "order_id")
    list_editable = ("status", "pay_status")
    list_filter = ("date_created", "status", "pay_status")
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "order_id",
    )
    inlines = [OrderItemInline]
