from rest_framework import serializers
from site_settings_app.models import (
    Setting,
    Phone,
    Social,
    About,
    Contact,
    Notification,
)


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"


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
