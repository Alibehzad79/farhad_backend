# Generated by Django 5.1.5 on 2025-02-02 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products_app", "0002_alter_category_parent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="parent",
        ),
    ]
