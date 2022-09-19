from django.urls import path

from .views import *

urlpatterns = [
    path("/signup", SignUpView.as_view()),
    path("/signin", SignInView.as_view()),
    path("", UserListView.as_view()),
    path('/<int:pk>', UserDetailView.as_view()),
]