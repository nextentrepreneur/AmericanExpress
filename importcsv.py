#This module can be used to upload csv file data to the sqlite database directly.
#To import the cse file data just execute this module: "python importcsv.py" 

import csv,sys,os

project_dir = "D:\AmericanExpress"

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'AmericanExpress.settings'

import django
django.setup()

from CreditCardStatement.models import CreditCard

#here the csv file name is "credit_card57066ea.csv",
#you can upload any csv file just include the name of that csv file

data = csv.reader(open("D:\\AmericanExpress\\credit_card57066ea.csv"),delimiter=',')

for row in data:
    if row[0] != 'ID':
        creditcard = CreditCard()
        creditcard.ID = row[0]
        creditcard.Name = row[1]
        creditcard.LIMIT_BAL = row[2]
        creditcard.SEX = row[3]
        creditcard.EDUCATION = row[4]
        creditcard.MARRIAGE = row[5]
        creditcard.AGE = row[6]
        creditcard.PAY_0 = row[7]
        creditcard.PAY_2 = row[8]
        creditcard.PAY_3 = row[9]
        creditcard.PAY_4 = row[10]
        creditcard.PAY_5 = row[11]
        creditcard.PAY_6 = row[12]
        creditcard.BILL_AMT1 = row[13]
        creditcard.BILL_AMT2 = row[14]
        creditcard.BILL_AMT3 = row[15]
        creditcard.BILL_AMT4 = row[16]
        creditcard.BILL_AMT5 = row[17]
        creditcard.BILL_AMT6 = row[18]
        creditcard.PAY_AMT1 = row[19]
        creditcard.PAY_AMT2 = row[20]
        creditcard.PAY_AMT3 = row[21]
        creditcard.PAY_AMT4 = row[22]
        creditcard.PAY_AMT5 = row[23]
        creditcard.PAY_AMT6 = row[24]
        creditcard.default_payment_next_month = row[25]
        creditcard.save()
