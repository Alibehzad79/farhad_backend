from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products_app"
    verbose_name = _("بخش محصولات")
