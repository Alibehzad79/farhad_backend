from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Setting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name=_("نام سایت"))
    site_logo = models.ImageField(upload_to="site/logos/", verbose_name=_("لوگوی سایت"))
    site_description = models.TextField(verbose_name=_("توضیحات درباره سایت"))

    class Meta:
        verbose_name = _("تنظیم")
        verbose_name_plural = _("تنظیمات")

    def __str__(self):
        return self.site_name


class Social(models.Model):
    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        verbose_name=_("تنظیم"),
        related_name="socials",
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("نام شبکه"),
        help_text=_("instagram, telegram, ..."),
    )
    link = models.URLField(
        verbose_name=_("لینک صفحه"),
        help_text=_("https://"),
    )

    def __str__(self):
        return self.name


class Phone(models.Model):
    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        verbose_name=_(
            "تنظیم",
        ),
        related_name="phones",
    )
    number = models.CharField(
        max_length=100,
        verbose_name=_("شماره تلفن"),
    )

    def __str__(self):
        return self.number


class About(models.Model):

    class Meta:
        verbose_name = _("درباره ما")
        verbose_name_plural = _("درباره ما ها")


class Contact(models.Model):

    class Meta:
        verbose_name = _("تماس")
        verbose_name_plural = _("تماس ها")


class Notification(models.Model):

    class Meta:
        verbose_name = _("اعلان")
        verbose_name_plural = _("اعلانات")
