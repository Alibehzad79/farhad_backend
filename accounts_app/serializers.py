from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator


class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[
            RegexValidator(
                regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,12}$",
                message="حداقل 6 و حداکثر 12 کاراکتر، حداقل یک حرف بزرگ، یک حرف کوچک، یک عدد و یک کاراکتر خاص",
            )
        ],
    )
    first_name = serializers.CharField(
        required=True,
        max_length=20,
    )
    last_name = serializers.CharField(
        required=True,
        max_length=20,
    )
    email = serializers.EmailField(
        max_length=256,
    )

    def validate_email(self, value):
        value = value.lower()
        check_exist_email = get_user_model().objects.filter(email=value).exists()
        if check_exist_email:
            raise serializers.ValidationError(
                "ایمیل وارد شده از قبل در سایت ثبت شده است."
            )

        return value
