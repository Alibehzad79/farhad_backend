# Generated by Django 5.1.5 on 2025-03-15 09:31

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("site_settings_app", "0003_rename_url_social_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="content",
            field=tinymce.models.HTMLField(default="", verbose_name="درباره ما"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="about",
            name="image",
            field=models.ImageField(
                default="", upload_to="images/about/", verbose_name="عکس"
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=100, verbose_name="نام")),
                (
                    "image",
                    models.ImageField(upload_to="images/team/", verbose_name="عکس"),
                ),
                (
                    "about",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="site_settings_app.about",
                        verbose_name="درباره ما",
                    ),
                ),
            ],
            options={
                "verbose_name": "تیم",
                "verbose_name_plural": "تیم ها",
            },
        ),
    ]
