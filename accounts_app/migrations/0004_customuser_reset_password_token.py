# Generated by Django 5.1.5 on 2025-02-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts_app", "0003_alter_customuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="reset_password_token",
            field=models.CharField(
                blank=True,
                max_length=32,
                null=True,
                verbose_name="توکن بازیابی رمز عبور",
            ),
        ),
    ]
