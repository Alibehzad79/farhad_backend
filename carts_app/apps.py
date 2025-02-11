from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CartsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "carts_app"
    verbose_name = _("بخش سبد خرید")
