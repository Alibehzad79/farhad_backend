from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import get_random_string
from products_app.models import Product

# Create your models here.


class Order(models.Model):
    STATUS = (
        ("not_paid", "پرداخت نشده"),
        ("paid", "پرداخت شده"),
        ("cancled", "لغو شده"),
    )

    order_id = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        unique=True,
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("کاربر"),
    )
    total_price = models.BigIntegerField(default=1, verbose_name=_("قیمت کل پرداختی"))
    user_info = models.TextField(verbose_name=_("اطلاعات تماس"))
    date_created = models.DateTimeField(
        auto_now_add=False, auto_now=False, verbose_name=_("تاریخ ایجاد")
    )
    status = models.CharField(max_length=100, choices=STATUS, default="not_paid")

    def save(self, *args, **kwargs):
        if self.order_id is None:
            self.order_id = get_random_string(32)
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        if self.user.first_name:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return self.user.username

    class Meta:
        verbose_name = _("سفارش")
        verbose_name_plural = _("سفارشات")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("سفارش"))
    porudct_name = models.CharField(max_length=100, verbose_name=_("نام محصول"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("مقدار"))
    price = models.BigIntegerField(default=1, verbose_name=_("قیمت کل"))

    def __str__(self):
        return self.porudct_name

    class Meta:
        verbose_name = _("محصول")
        verbose_name_plural = _("محصولات")
