from django.urls import path

from .views import *

urlpatterns = [
    path("/signup", SignUpView.as_view()), # 회원가입
    path("/signin", SignInView.as_view()), # 로그인
    path("", UserListView.as_view()), # 회원 정보 조회
    path('/<int:pk>', UserDetailView.as_view()), # 회원 정보 수정/삭제
]