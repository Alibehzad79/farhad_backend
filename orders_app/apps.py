from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrdersAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "orders_app"
    verbose_name = _("بخش سفارشات")
