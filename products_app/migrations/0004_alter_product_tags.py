# Generated by Django 5.1.5 on 2025-02-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products_app", "0003_remove_category_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(
                related_name="tags", to="products_app.tag", verbose_name="برچسب ها"
            ),
        ),
    ]
