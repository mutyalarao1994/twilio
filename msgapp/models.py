from unittest import result
from django.db import models
import os
from twilio.rest import Client

# Create your models here.
class Marks(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(self.result)

    def save(self,*args,**kwargs):
        print(args,'gggggggggggggg',kwargs)
        account_sid = 'AC4fd56c885b924a0f0f2af3cb4a3573e8'
        auth_token = '32a66d0378471fa4569c30ef1ecfb361'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body='Dear Customer, Acct XX856 is credited with Rs 37100.00 on 01-Jul-22 from HAREESH GARA HGIN. UPI:218222650105-ICICI Bank.',
                                    from_='+15672293605',
                                    to='+916300023235'
                                )

        print(message.sid,'jjjjjjjjjjjjjj')
        print(args,'aaaaaaaaaaaaaaaaaa',kwargs)
        return super(Marks,self).save(*args,**kwargs)
