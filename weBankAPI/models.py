from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

ACCOUNT_TYPE = (
    ('SAVINGS', 'savings'),
    ('CURRENT', "current"),
)


# Create your models here.
class Accounts(models.Model):
    # customer_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account_no = models.IntegerField(validators=[MinLengthValidator(10),MaxLengthValidator(10)])
    account_type = models.CharField(max_length=40, choices=ACCOUNT_TYPE)
    account_balance = models.FloatField(default=0)
    
    def __str__(self):
        return self.account_no
    
