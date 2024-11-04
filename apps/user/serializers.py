from rest_framework import serializers


class OtpSerializer(serializers.Serializer):
    code = serializers.CharField()
