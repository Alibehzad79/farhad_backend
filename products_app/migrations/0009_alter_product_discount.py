# Generated by Django 5.1.5 on 2025-02-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products_app", "0008_alter_product_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="discount",
            field=models.FloatField(default=0, verbose_name="درصد تخفیف"),
        ),
    ]
