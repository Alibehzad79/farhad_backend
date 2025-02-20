# Generated by Django 5.1.5 on 2025-02-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders_app", "0002_orderitem_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("not_paid", "پرداخت نشده"),
                    ("paid", "پرداخت شده"),
                    ("cancled", "لغو شده"),
                ],
                default="not_paid",
                max_length=100,
            ),
        ),
    ]
