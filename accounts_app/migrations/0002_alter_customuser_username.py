# Generated by Django 5.1.5 on 2025-01-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="نام کاربری"
            ),
        ),
    ]
