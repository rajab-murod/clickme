import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from clickme.serializers import *
from clickme.config import Config
from clickme.models import Transaction


class CardCreateApiView(APIView):
    def __init__(self):
        self.conf = Config()
        super(CardCreateApiView, self).__init__()

    def post(self, request):
        serializer = CardCreateSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        result = self.card_create(serializer.validated_data)

        return Response(result)

    def card_create(self, validated_data):

        data = dict(
            service_id=self.conf.SERVICE_ID,
            card_number=validated_data['card_number'],
            expire_date=validated_data['expire_date'],
            temporary=validated_data['temporary'],
        )

        response = requests.post(self.conf.CARD_CREATE_URL, json=data, headers=self.conf.HEADER)
        result = response.json()

        return result


class CardVerifyApiView(APIView):
    def __init__(self):
        self.conf = Config()
        super(CardVerifyApiView, self).__init__()

    def post(self, request):
        serializer = CardVerifySerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        result = self.card_verify(serializer.validated_data)

        return Response(result)

    def card_verify(self, validated_data):
        data = dict(
            service_id=self.conf.SERVICE_ID,
            card_token=validated_data['card_token'],
            sms_code=validated_data['sms_code'],
        )

        response = requests.post(self.conf.CARD_VERIFY_URL, json=data, headers=self.conf.HEADER)
        result = response.json()

        return result


class PaymentApiView(APIView):
    def __init__(self):
        self.conf = Config()
        super(PaymentApiView, self).__init__()

    def post(self, request):
        serializer = PaymentSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        result = self.payment(serializer.validated_data)

        return Response(result)

    def payment(self, validated_data):
        data = dict(
            service_id=self.conf.SERVICE_ID,
            card_token=validated_data['card_token'],
            amount=validated_data['amount'],
            transaction_parameter=validated_data['trans_id'],
        )

        response = requests.post(self.conf.PAYMENT_URL, json=data, headers=self.conf.HEADER)
        result = response.json()

        return result