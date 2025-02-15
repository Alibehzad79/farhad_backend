from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WishlistAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wishlist_app"
    verbose_name = _("بخش علاقه مندی ها")
