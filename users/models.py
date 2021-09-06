from django.db import models

class Transaction(models.Model):
    cryptoType= models.CharField(max_length=200)
    intention= models.CharField(max_length=200)
    quantity= models.IntegerField(default=0)
    pub_date = models.CharField(max_length=200)
    belongs_to = models.IntegerField(null = True)

    def __str__(self):
        return f'{self.intention}: {self.quantity} of {self.cryptoType}'
