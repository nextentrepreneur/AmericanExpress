from django.db import models

# Create your models here.
class CreditCard(models.Model):
    #user details field
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    LIMIT_BAL   = models.IntegerField()
    SEX = models.IntegerField()
    EDUCATION = models.IntegerField()
    MARRIAGE = models.IntegerField()
    AGE = models.IntegerField()

    #Repayment Status model field
    PAY_0 = models.IntegerField()
    PAY_2 = models.IntegerField()
    PAY_3 = models.IntegerField()
    PAY_4 = models.IntegerField()
    PAY_5 = models.IntegerField()
    PAY_6 = models.IntegerField()

    #Amount of Bill Statement
    BILL_AMT1 = models.IntegerField()
    BILL_AMT2 = models.IntegerField()
    BILL_AMT3 = models.IntegerField()
    BILL_AMT4 = models.IntegerField()
    BILL_AMT5 = models.IntegerField()
    BILL_AMT6 = models.IntegerField()

    # Amount of Previous payment
    PAY_AMT1 = models.IntegerField()
    PAY_AMT2 = models.IntegerField()
    PAY_AMT3 = models.IntegerField()
    PAY_AMT4 = models.IntegerField()
    PAY_AMT5 = models.IntegerField()
    PAY_AMT6 = models.IntegerField()

    default_payment_next_month = models.IntegerField()

    def __str__(self):
        return self.Name
