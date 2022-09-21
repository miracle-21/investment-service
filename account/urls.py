from django.urls import path

from .views import *

urlpatterns = [
    path("/<int:id>", InvestmentListView.as_view()), # 투자 화면/투자상세 화면
    path("/asset/<int:id>", HoldingListView.as_view()), # 보유종목 화면
    path("/invest/<int:id>", TransferRequestView.as_view()), # 입금 거래 정보 등록
    path("/invest/transfer/<int:id>", TransferView.as_view()), # 입금 거래
]