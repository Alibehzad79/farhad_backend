from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from django.core import validators

from config import settings
from django.core.mail import send_mail
from django.core.exceptions import ValidationError


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
    STATUS = (
        ("answered", "جواب داده شده"),
        ("pending", "در انتظار بررسی"),
    )
    first_name = models.CharField(
        max_length=25,
        verbose_name=_("نام"),
    )
    last_name = models.CharField(
        max_length=25,
        verbose_name=_("نام خانوادگی"),
    )
    email = models.EmailField(
        verbose_name=_("ایمیل"),
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name=_("شماره تلفن"),
        validators=[
            validators.RegexValidator(regex="^[0-9]+$", message="باید عدد باشد.")
        ],
    )
    subject = models.CharField(
        max_length=100,
        verbose_name=_("عنوان"),
    )
    message = models.TextField(
        verbose_name=_("پیام"),
    )
    date_created = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name=_("تاریخ ایجاد"),
    )
    answer = models.TextField(verbose_name=_("جواب"), blank=True, null=True)
    status = models.CharField(
        max_length=100,
        choices=STATUS,
        default="pending",
        verbose_name=_("وضعیت"),
    )

    def save(self, *args, **kwargs):
        if self.status == "answered":
            # send notification in email and phone number
            try:
                send_mail(
                    subject=f"به تماس شما جواب داده شد.",
                    message=f"{self.answer}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[self.email],
                )
            except:
                raise ValidationError(
                    {"email": "هیچ محصولی در این دسته بندی یافت نشد."}
                )
        super(Contact, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("تماس")
        verbose_name_plural = _("تماس ها")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Notification(models.Model):

    class Meta:
        verbose_name = _("اعلان")
        verbose_name_plural = _("اعلانات")
