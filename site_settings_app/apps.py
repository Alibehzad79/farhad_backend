from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SiteSettingsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "site_settings_app"
    verbose_name = _("تنظیمات سایت")
