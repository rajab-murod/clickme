from django.db import models


class Transaction(models.Model):
    PROCESS = 0
    PAID = 1
    FAILED = 2
    STATUS = (
        (PROCESS, 'processing'),
        (PAID, 'paid'),
        (FAILED, 'failed'),
    )

    payment_id = models.CharField(max_length=255)
    request_id = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    status = models.CharField(max_length=10, default=PROCESS, choices=STATUS)
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(auto_now=True)

    def create_transaction(self, payment_id, request_id, amount, status):
        Transaction.objects.create(
            payment_id=payment_id,
            request_id=request_id,
            amount=amount / 100,
            status=status
        )

    def update_transaction(self, payment_id, status):
        trans = Transaction.objects.get(payment_id=payment_id)
        trans.status = status
        trans.save()