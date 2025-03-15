from rest_framework import serializers
from site_settings_app.models import (
    Setting,
    Phone,
    Social,
    About,
    Team,
    Contact,
    Notification,
)
from config import settings


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = "__all__"

    def get_image(self, obj):
        return f"{settings.BACKEND_URL}/{obj.image.url}"


class SettingSerializer(serializers.ModelSerializer):
    socials = serializers.SerializerMethodField()
    phones = serializers.SerializerMethodField()

    class Meta:
        model = Setting
        fields = "__all__"

    def get_socials(self, obj):
        return (SocialSerializer(social).data for social in obj.socials.all())

    def get_phones(self, obj):
        return (PhoneSerializer(phone).data for phone in obj.phones.all())


class AboutSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    teams = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = "__all__"

    def get_image(self, obj):
        return f"{settings.BACKEND_URL}/{obj.image.url}"

    def get_teams(self, obj):
        return (TeamSerializer(team).data for team in obj.teams.all())
