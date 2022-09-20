from django.urls import path

from .views import *

urlpatterns = [
    path("/invest/<int:id>", InvestmentListView.as_view()),
    path("/asset/<int:id>", HoldingListView.as_view()),
]