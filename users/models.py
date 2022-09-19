from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    "유저 매니저 정의"
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("계정이름을 입력해주세요.")
        if not password:
            raise ValueError("비밀번호를 입력해주세요.")
        if not email:
            raise ValueError("이메일을 입력해주세요.")

        user = self.model(
            username = username,
            password = password,
            email = email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username = username,
            password = password,
            email = email,
        )

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractUser):
    """유저 모델"""
    username = models.CharField(verbose_name="ID", max_length=20, unique=True)
    name     = models.CharField(verbose_name="이름", max_length=100)
    email    = models.CharField(verbose_name="이메일", max_length=100)

    # status
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # except
    first_name = None
    last_name = None

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "email"]

    class Meta:
        db_table = "users"