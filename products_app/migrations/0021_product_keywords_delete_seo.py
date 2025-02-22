# Generated by Django 5.1.5 on 2025-02-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products_app", "0020_alter_seo_keywords"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="keywords",
            field=models.TextField(
                blank=True,
                help_text="مثال: چاقو، موبایل، ...",
                null=True,
                verbose_name="Keywords",
            ),
        ),
        migrations.DeleteModel(
            name="Seo",
        ),
    ]
