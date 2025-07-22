from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
import random

from .models import User, OTP
from .serializers import UserSerializer, RequestOTPSerializer, VerifyOTPSerializer

from rest_framework_simplejwt.tokens import RefreshToken


# Helper to generate OTP
def generate_otp():
    return f"{random.randint(100000, 999999)}"


# Helper to generate JWT
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful. Please verify your email."}, status=201)
        return Response(serializer.errors, status=400)


class RequestOTPView(APIView):
    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user, _ = User.objects.get_or_create(email=email)

            # 🔐 Rate limit: max 3 OTPs per 10 minutes
            ten_minutes_ago = timezone.now() - timedelta(minutes=10)
            otp_count = OTP.objects.filter(user=user, created_at__gte=ten_minutes_ago).count()

            if otp_count >= 3:
                return Response({"message": "Too many OTP requests. Try again after 10 minutes."}, status=429)

            code = generate_otp()
            expires_at = timezone.now() + timedelta(minutes=5)

            OTP.objects.create(user=user, code=code, expires_at=expires_at)

            # Mock email service: just print the OTP to console
            print(f"OTP for {email}: {code}")

            return Response({"message": "OTP sent to your email."}, status=200)
        return Response(serializer.errors, status=400)


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            otp_obj = serializer.validated_data['otp_obj']
            otp_obj.is_verified = True
            otp_obj.save()

            token = get_tokens_for_user(otp_obj.user)

            return Response({"message": "Login successful.", "token": token}, status=200)
        return Response(serializer.errors, status=400)
