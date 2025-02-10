from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=256, verbose_name=_("ایمیل"), unique=True)
    reset_password_token = models.CharField(
        max_length=32,
        verbose_name=_("توکن بازیابی رمز عبور"),
        blank=True,
        null=True,
        unique=True,
    )
    phone_number = models.CharField(
        max_length=11, blank=True, null=True, verbose_name=_("شماره تلفن")
    )
    address = models.TextField(blank=True, null=True, verbose_name=_("آدرس"))
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
