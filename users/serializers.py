from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


"""로그인"""
class SignInSerializer(TokenObtainPairSerializer):
    def validate(self, data):
        """로그인 유효성 검사"""
        username = data.get("username")
        password = data.get("password")

        user = User.objects.get(username=username)

        if user:
            if not user.is_active:
                raise serializers.ValidationError("비활성화된 계정입니다.")

            if not user.check_password(password):
                raise serializers.ValidationError("아이디 또는 비밀번호를 잘못 입력했습니다.")
        else:
            raise serializers.ValidationError("아이디 또는 비빌먼호를 잘못 입력했습니다.")

        token = super().get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)

        data = {
            "access" : access_token,
            "refresh" : refresh_token,
        }
        return data


"""회원가입"""
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
        ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user