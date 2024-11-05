import pdb

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, VerifyOTPSerializer, AuthSerializer
from django.utils.crypto import get_random_string
from .nikita import send_sms
from drf_spectacular.utils import extend_schema

User = get_user_model()


def _generate_verification_code():
    return get_random_string(4, allowed_chars='123456789')


@extend_schema(tags=['Auth'])
class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        otp_code = _generate_verification_code()

        user_data = {
            'phone_number': phone_number,
            'first_name': serializer.validated_data.get('first_name', ''),
            'last_name': serializer.validated_data.get('last_name', ''),
            'email': serializer.validated_data.get('email', ''),
            'birth_date': serializer.validated_data.get('birth_date', None),
            'avatar': serializer.validated_data.get('avatar', ''),
            'is_active': False,
            'code': otp_code,
        }

        User.objects.create_user(**user_data)
        message = "OTP sent."

        send_sms(phone_number, otp_code)
        return Response({"message": message}, status=status.HTTP_201_CREATED)


@extend_schema(tags=['Auth'])
class AuthenticationUserView(GenericAPIView):
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']

        user = User.objects.filter(phone_number=phone_number)
        if not user.exists():
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        otp_code = _generate_verification_code()
        send_sms(phone_number, otp_code)
        user = user.first()
        user.code = otp_code
        user.save()
        return Response({"message": phone_number}, status=status.HTTP_200_OK)


@extend_schema(tags=['Auth'])
class VerifyOtpView(GenericAPIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        otp_code = serializer.validated_data['otp_code']

        user = User.objects.get(phone_number=phone_number)
        if user.code != otp_code:
            return Response({'message': 'Invalid cred'}, status=status.HTTP_403_FORBIDDEN)

        user.is_active = True
        user.code = None
        user.save()
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)
