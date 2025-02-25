# Generated by Django 5.1.5 on 2025-02-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products_app", "0023_alter_product_visit_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="visit_count",
            field=models.BigIntegerField(
                default=0, editable=False, verbose_name="تعداد بازدید"
            ),
        ),
    ]
