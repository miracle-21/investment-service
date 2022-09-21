from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers import RegisterSerializer, SignInSerializer
from users.models import User


class SignInView(APIView):
    '''
    회원가입
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data
            return Response(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class SignUpView(CreateAPIView):
    '''
    로그인
    NOTICE: 발급받은 토큰을 이용해 권한 설정을 해야했지만 아직 구현하지 못한 상태다.
    '''
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserListView(generics.ListAPIView):
    '''
    회원정보조회
    NOTICE: 필터링 기능은 없다. 전체 회원 조회만 가능하다.
    '''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    회원정보수정/삭제
    '''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer