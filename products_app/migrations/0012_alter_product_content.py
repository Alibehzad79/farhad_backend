# Generated by Django 5.1.5 on 2025-02-06 12:44

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products_app", "0011_setdiscount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="content",
            field=tinymce.models.HTMLField(verbose_name="توضیحات کامل"),
        ),
    ]
