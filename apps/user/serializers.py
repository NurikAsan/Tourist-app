from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'phone_number',
            'first_name', 'last_name',
            'email', 'birth_date',
            'avatar'
        )

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Номер телефона уже существует")
        return value


class AuthSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)


class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    otp_code = serializers.CharField(required=True, min_length=4)
