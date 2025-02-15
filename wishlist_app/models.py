from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from products_app.models import Product

# Create your models here.


class Wishlist(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("کاربر")
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("محصول")
    )
    date_add = models.DateTimeField(
        auto_now=False, auto_now_add=False, verbose_name=_("تاریخ اضافه شدن")
    )

    def __str__(self):
        return self.product.title

    def clean(self):
        if Wishlist.objects.filter(user=self.user, product=self.product).exists():
            raise ValidationError("محصول از قبل در لیست علاقه مندی ها موجود است.")

    class Meta:
        verbose_name = _("علاقمه مندی")
        verbose_name_plural = _("لیست علاقه مندی ها")
