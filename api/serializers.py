from rest_framework import serializers
from .models import User, OTP
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

class RequestOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Email not registered.")

        otp_obj = OTP.objects.filter(user=user, code=data['otp'], is_verified=False).order_by('-created_at').first()

        if not otp_obj:
            raise serializers.ValidationError("Invalid OTP.")
        if otp_obj.is_expired():
            raise serializers.ValidationError("OTP has expired.")

        data['user'] = user
        data['otp_obj'] = otp_obj
        return data
