from django.db import models
from users.models import User

class Holding(models.Model):
    name          = models.CharField(max_length=100) # 종목명
    isin          = models.CharField(max_length=50)
    current_price = models.DecimalField(max_digits=15, decimal_places=2, default=0) # 현재가
    asset_group   = models.CharField(max_length=100) # 자산그룹
    
    class Meta:
        db_table = 'holdings'

    def __str__(self):
        return self.name


class UserHolding(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    holding   = models.ForeignKey(Holding, on_delete=models.CASCADE)
    quantity  = models.IntegerField() # 보유수량
    
    class Meta:
        db_table = 'user_holdings'

    def __str__(self):
        return str(self.quantity)


class Account(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name   = models.CharField(max_length=100) # 계좌명
    account_number = models.IntegerField() # 계좌번호
    total_assests  = models.DecimalField(max_digits=15, decimal_places=2, default=0) # 총자산
    
    class Meta:
        db_table = 'accounts'

    def __str__(self):
        return self.account_name

class Investment(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    company   = models.CharField(max_length=100) # 증권사
    principal = models.DecimalField(max_digits=15, decimal_places=2, default=0) # 투자원금
    
    class Meta:
        db_table = 'investments'

    def __str__(self):
        return self.company