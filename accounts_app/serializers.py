from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator


class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True,
        write_only=True,
        min_length=8,
    )
    first_name = serializers.CharField(
        required=True,
        max_length=20,
        min_length=3,
    )
    last_name = serializers.CharField(
        required=True,
        max_length=20,
        min_length=3,
    )
    email = serializers.EmailField(
        max_length=256,
        required=True,
    )

    def validate_email(self, value):
        value = value.lower()
        check_exist_email = get_user_model().objects.filter(email=value).exists()
        if check_exist_email:
            raise serializers.ValidationError(
                "ایمیل وارد شده از قبل در سایت ثبت شده است."
            )

        return value


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        value = value.lower()
        if not get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("کاربری با این ایمیل یافت نشد.", code=404)
        return value


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, required=True)
    token = serializers.CharField(min_length=32, max_length=32, required=True)

    def validate_token(self, value):
        if not get_user_model().objects.filter(reset_password_token=value).exists():
            raise serializers.ValidationError("توکن نامعتبر")
        return value


class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        exclude = ("password", "reset_password_token")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class EditUserDetailSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        required=True,
    )
    last_name = serializers.CharField(
        required=True,
    )
    address = serializers.CharField(
        required=True,
    )
    phone_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex="^[0-9]+$",
                message="نوع باید عدد باشد.",
            )
        ],
        max_length=11,
        min_length=11,
        required=True,
    )
