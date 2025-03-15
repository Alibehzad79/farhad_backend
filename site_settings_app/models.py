from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

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
    image = models.ImageField(upload_to="images/about/", verbose_name=_("عکس"))
    content = HTMLField(verbose_name=_("درباره ما"))

    class Meta:
        verbose_name = _("درباره ما")
        verbose_name_plural = _("درباره ما ها")

    def __str__(self):
        return str(_("درباره ما"))


class Team(models.Model):
    about = models.ForeignKey(
        About,
        on_delete=models.CASCADE,
        verbose_name=_("درباره ما"),
        related_name="teams",
    )
    name = models.CharField(max_length=100, verbose_name=_("نام"))
    image = models.ImageField(upload_to="images/team/", verbose_name=_("عکس"))

    class Meta:
        verbose_name = _("تیم")
        verbose_name_plural = _("تیم ها")

    def __str__(self):
        return self.name


class Contact(models.Model):

    class Meta:
        verbose_name = _("تماس")
        verbose_name_plural = _("تماس ها")


class Notification(models.Model):

    class Meta:
        verbose_name = _("اعلان")
        verbose_name_plural = _("اعلانات")
