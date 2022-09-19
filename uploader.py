import os
import django
import csv
import sys

from django.db import IntegrityError, transaction

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", 
    "service.settings"
)
django.setup()

from users.models      import User
from account.models    import *

CSV_PATH_ACCOUNT_ASSET = './csv/account_asset_info_set.csv'
CSV_PATH_ACCOUNT_BASIC = './csv/account_basic_info_set.csv'
CSV_PATH_ASSET_GROUP = './csv/asset_group_info_set.csv'


try:
    with transaction.atomic():
        """
        account_asset_info_set uploader
        """
        with open(CSV_PATH_ACCOUNT_ASSET) as in_file:
            data_reader = csv.reader(in_file)
            for row in data_reader:
                if row[0]:
                    username = row[0]
                    company = row[1]
                    account_number = row[2]
                    account_name = row[3]
                    isin=row[4]
                    current_price = row[5]
                    quantity = row[6]

                '''
                investment
                '''
                for user in User.objects.filter(username=username):
                    if company not in [i.company for i in Investment.objects.filter(user_id=user.id).filter(company=company)]:
                        Investment.objects.create(
                            user_id = user.id,
                            company = company
                        )
                '''
                account
                '''
                for user in User.objects.filter(username=username):
                    if account_name not in [i.account_name for i in Account.objects.filter(user_id=user.id).filter(account_name=account_name)]:
                        Account.objects.create(
                            user_id = user.id,
                            account_name = account_name,
                            account_number = account_number
                        )
                '''
                holding
                '''
                for i in Holding.objects.filter(isin=isin):
                    i.current_price = current_price
                    i.save()

                for i in Holding.objects.filter(isin=isin):
                    UserHolding.objects.create(
                        user_id = User.objects.get(username=username).id,
                        holding_id = i.id,
                        quantity = quantity
                    )

        """
        account_basic_info_set uploader
        # investment principal
        # """
        with open(CSV_PATH_ACCOUNT_BASIC) as in_file:
            data_reader = csv.reader(in_file)
            for row in data_reader:
                if row[0]:
                    account_number = row[0]
                    principal = row[1]
                
                for i in Account.objects.filter(account_number=account_number):
                    investment = Investment.objects.filter(user_id=i.user_id)
                    for i in investment:
                        i.principal = principal
                        i.save()

        """
        asset_group_info_set uploader
        """
        with open(CSV_PATH_ASSET_GROUP) as in_file:
            data_reader = csv.reader(in_file)
            for row in data_reader:
                if row[0]:
                    name = row[0]
                    isin = row[1]
                    asset_group = row[2]
                
                Holding.objects.create(
                    name = name,
                    isin = isin,
                    asset_group = asset_group
        #         )
except IntegrityError:
    raise IntegrityError