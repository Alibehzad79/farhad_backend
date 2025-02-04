from django.contrib import admin, messages
from products_app.models import Category, Tag, Product, Gallery, SetDiscount
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "discount",
        "discount_price",
        "date_created",
        "status",
    )
    list_editable = ("status",)
    list_filter = ("date_created", "category")
    search_fields = ("title", "short_description", "content")
    inlines = [
        GalleryInline,
    ]


@admin.register(SetDiscount)
class SetDiscountAdmin(admin.ModelAdmin):
    list_display = (
        "discount",
        "category",
        "delete_button",
        "re_submit",
    )
    list_editable = ("category",)
    list_filter = ("category",)
    search_fields = ("category__name", "category__slug")
    actions = None

    def delete_button(self, obj):
        delete_url = reverse(
            "admin:%s_%s_delete" % (obj._meta.app_label, obj._meta.model_name),
            args=[obj.pk],
        )
        return format_html(
            '<a href="{}" class="button" style="color:red; background-color: transparent; border: 1px solid gray;">حذف کردن</a>',
            delete_url,
        )

    def re_submit(self, obj):
        submit = obj.save()
        return format_html(
            '<a href="/admin/products_app/setdiscount/" class="button" style="color:blue; background-color: transparent; border: 1px solid gray;">اعمال دوباره</a>',
            submit,
        )

    delete_button.short_description = "حذف"
    re_submit.short_description = "اعمال دوباره"


admin.site.register(Category)
admin.site.register(Tag)
