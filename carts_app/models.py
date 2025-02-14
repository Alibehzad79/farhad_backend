from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from products_app.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="carts",
        verbose_name=_("کاربر"),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("محصول"),
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name=_("مقدار"),
        validators=[
            validators.MinValueValidator(1, "کمترین مقدار باید عدد 1 باشد."),
        ],
    )

    def total_price(self):
        if self.product.discount > 0:
            return self.product.discount_price() * self.quantity
        else:
            return self.quantity * self.product.price

    total_price.short_description = "جمع قیمت"

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _("سبد خرید")
        verbose_name_plural = _("سبد خریدها")

    def clean(self):
        if Cart.objects.filter(product=self.product, user=self.user).exists():
            carts = Cart.objects.filter(product=self.product, user=self.user).all()
            for cart in carts:
                cart.delete()
