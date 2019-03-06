from django.db import models

# Create your models here.
class Stocks_Details(models.Model):
    company_name=models.CharField(max_length=100)
    medicine=models.CharField(max_length=250)
    price=models.IntegerField()
    quantity=models.IntegerField()
