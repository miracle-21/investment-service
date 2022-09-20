import json

from django.http      import JsonResponse
from django.views     import View

from users.models import User
from account.models import Holding

class InvestmentListView(View):
    def get(self, request, id):
        '''
        투자 화면/투자상세 화면
        '''
        user = User.objects.get(id=id)
        account = user.account_set.get(user_id=id)
        investment = user.investment_set.get(user_id=id)

        results = {
                'user_id' : user.id,
                'account_name' :account.account_name,
                'company' : investment.company,
                'account_number' :account.account_number,
                'total_assests' : int(account.total_assests),
                'total_profit' : int(account.total_assests) - int(investment.principal),
                'rate' : (int(account.total_assests) - int(investment.principal))/int(investment.principal)*100,
            }
    
        return JsonResponse({'results' : results}, status = 200)

class HoldingListView(View):
    def get(self, request, id):
        '''
        보유종목 화면
        '''
        user = User.objects.get(id=id)
        userholding = user.userholding_set.get(user_id=id)

        results = {
                'user_id' : id,
                'holding_name' : userholding.holding.name,
                'asset_group' : userholding.holding.asset_group,
                'market_value' : int(userholding.holding.current_price),
                'isin' : userholding.holding.isin
            }
    
        return JsonResponse({'results' : results}, status = 200)

'''
보유 종목명
보유 종목의 자산군
보유 종목의 평가 금액 (종목 보유 수량 * 종목 현재가)
보유 종목 ISIN
'''