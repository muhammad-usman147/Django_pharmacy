from django.shortcuts import render
from django.http import HttpResponse
from .models import Stocks_Details
# Create your views here.
def show(request):
    sd=Stocks_Details.objects.all()
    return render(request,'details.html',{'sd_d':sd})