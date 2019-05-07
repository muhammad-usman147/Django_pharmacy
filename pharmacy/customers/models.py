from django.db import models
from stocks.models import Stocks_Details
# Create your models here.
class Bill(models.Model):
    name=models.CharField(max_length=30)
    medi=models.CharField(max_length=30)
    total=models.IntegerField()
    qty=models.IntegerField()

    
