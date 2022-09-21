import json
import bcrypt
import jwt

from django.http    import JsonResponse
from django.views   import View
from account.models import HoldingsRegist, Holding, Account, FinalHolding

from users.models import User
from account.hash import *
from my_settings  import ALGORITHM, SECRET_KEY

class InvestmentListView(View):
    def get(self, request, id):
        '''
        투자 화면/투자상세 화면
        endpoint: /<int:user_id>
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
        endpoint: /asset/<int:user_id>
        '''
        user = User.objects.get(id=id)
        finalholdings = user.finalholding_set.filter(user_id=id)

        results = [{
                'user_id' : id,
                'holding_name' : finalholding.holding.name,
                'asset_group' : finalholding.holding.asset_group,
                'market_value' : int(finalholding.holding.current_price),
                'isin' : finalholding.holding.isin
            }for finalholding in finalholdings]
    
        return JsonResponse({'results' : results}, status = 200)

class TransferRequestView(View):
    def post(self, request, id):
        '''
        입금 거래 정보들을 서버에 등록. 입금 거래 전 필수 사항
        endpoint: /invest/<int:user_id>
        '''
        try:
            data = json.loads(request.body)

            account_number = str(data['account_number'])
            username = data['username']
            item = data['item']
            transfer_amount = data['transfer_amount']

            if User.objects.get(id=id).username != username:
                return JsonResponse({'message' : '권한이 없습니다'}, status = 401)
            else:
                # signature  = bcrypt.hashpw(account_number.encode('utf-8'), bcrypt.gensalt())
                signature  = jwt.encode({'account_number':account_number}, SECRET_KEY, algorithm=ALGORITHM).decode("utf-8")
                HoldingsRegist.objects.create(
                    user_id  = id,
                    holding_id = Holding.objects.get(name=item).id,
                    signature = signature,
                    transfer_identifier = save_data_hash_table(signature, transfer_amount),
                )
                return JsonResponse({"message" : "정보 등록 완료"}, status = 201)
        except User.DoesNotExist:
            return JsonResponse({'message' : '존재하지 않는 회원입니다'}, status = 401)

class TransferView(View):
    def get(self, request, id):
        '''
        입금 거래 정보 검증 후, 고객의 총 자산을 업데이트한다.
        자산 업데이트 후 입금 거래 정보는 삭제된다.
        endpoint: /invest/transfer/<int:id>
        '''
        try:
            regist = HoldingsRegist.objects.get(user_id=id)
            holding_id = regist.holding_id
            signature = regist.signature
            transfer_amount = regist.transfer_identifier
            account_number = int(list(jwt.decode(signature, SECRET_KEY, algorithms = ALGORITHM).values())[0])
            quantity = get_data_hash_table(signature, transfer_amount)
            price = Holding.objects.get(id=holding_id).current_price

            FinalHolding.objects.create(
                user_id  = id,
                holding_id =holding_id,
                quantity = quantity
            )

            account = Account.objects.filter(user_id=id).get(account_number=account_number)
            pre_assests = account.total_assests
            account.total_assests += price

            account.save()

            regist.delete()

            return JsonResponse({'주문 전 총자산' : int(pre_assests), '주문 후 총자산': int(account.total_assests)}, status = 200)

        except User.DoesNotExist:
            return JsonResponse({'message' : '존재하지 않는 회원입니다'}, status = 401)