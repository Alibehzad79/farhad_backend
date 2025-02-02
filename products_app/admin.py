from django.contrib import admin
from products_app.models import Category, Tag, Product, Gallery


# Register your models here.


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "date_created", "status")
    list_editable = ("status",)
    list_filter = ("date_created", "category")
    search_fields = ("title", "short_description", "content")
    inlines = [
        GalleryInline,
    ]


admin.site.register(Category)
admin.site.register(Tag)
