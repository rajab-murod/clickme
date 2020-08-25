from django.conf import settings

DEBUG = settings.PAYME_SETTINGS['DEBUG']
AUTHORIZATION = {'X-Auth': settings.PAYME_SETTINGS['MERCHANT_ID']}
KEY_1 = settings.PAYME_SETTINGS['ACCOUNTS']['KEY_1']
KEY_2 = settings.PAYME_SETTINGS['ACCOUNTS'].get('KEY_2', 'order_type')
TEST_URL = 'https://checkout.test.paycom.uz/api/'
PRO_URL = 'https://checkout.paycom.uz/api/'
URL = TEST_URL if DEBUG else PRO_URL