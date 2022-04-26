from django.db import models

DEPOSIT = 'Deposit'
WITHDRAWAL = 'Withdrawal'

TRANSACTION_TYPE_CHOICES = (
    (DEPOSIT, 'Deposit'),
    (WITHDRAWAL, 'Withdrawal'),
)

class Transaction(models.Model):
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # staff_id = models.ForeignKey(Agent, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    transaction_type = models.CharField(max_length= 20, choices=TRANSACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.transaction_type)

    class Meta:
        ordering = ['-timestamp']

class Report(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=50)
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.report_name