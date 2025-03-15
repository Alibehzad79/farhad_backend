from django.contrib import admin
from site_settings_app.models import Setting, Social, Phone, About, Team

# Register your models here.


class SocialInline(admin.TabularInline):
    model = Social
    extra = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


class TeamInline(admin.TabularInline):
    model = Team
    extra = 1


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ("site_name",)
    inlines = [SocialInline, PhoneInline]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    inlines = [TeamInline]
