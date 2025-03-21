# Generated by Django 5.1.5 on 2025-02-18 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "porudct_name",
                    models.CharField(max_length=100, verbose_name="نام محصول"),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(default=1, verbose_name="مقدار"),
                ),
                ("price", models.BigIntegerField(default=1, verbose_name="قیمت کل")),
            ],
            options={
                "verbose_name": "محصول",
                "verbose_name_plural": "محصولات",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_id",
                    models.CharField(blank=True, max_length=32, null=True, unique=True),
                ),
                ("user_info", models.TextField(verbose_name="اطلاعات تماس")),
                (
                    "total_price",
                    models.BigIntegerField(default=1, verbose_name="قیمت کل پرداختی"),
                ),
                ("date_created", models.DateTimeField(verbose_name="تاریخ ایجاد")),
                (
                    "status",
                    models.CharField(
                        choices=[("not_paid", "پرداخت نشده"), ("paid", "پرداخت شده")],
                        default="not_paid",
                        max_length=100,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "سفارش",
                "verbose_name_plural": "سفارشات",
            },
        ),
    ]
