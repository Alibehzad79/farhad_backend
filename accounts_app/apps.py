from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts_app"
    verbose_name = _("بخش اکانت ها")
