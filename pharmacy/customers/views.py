from django.shortcuts import render,redirect
from .models import Bill
from stocks.models import Stocks_Details
from django.http import HttpResponse
from . import form
# Create your views here.
def home(request):
    #forma=UserData.objects.all()
    forma=Stocks_Details.objects.all()
    forms=form.CreateUser()
    return render(request,'customers/chome.html',{'cdata':forms, 'forma':forma})
def save(request): 
    if request.method=='POST':
        bills=Bill()
        bills.name=request.POST.get('name')
        bills.medi=request.POST.get('medi')
        l=bills.medi
        bills.qty=request.POST.get('qty')
        q=bills.qty
        #stock_medi=Stocks_Details.objects.get(medicine=l).values(price)
        #dtl=Stocks_Details.objects.filter(medicine=l)
        #bills.total=(dtl.price*q)
        #pr=request.POST.get('total')
        prce=Stocks_Details.objects.get(medicine=l).price
        qty=request.POST.get('qty')
        p=(int(qty)*prce)
        context={
            'name':request.POST.get('name'),
            'medi':request.POST.get('medi'),
            'qty':qty,
            'price':p
        }
        return render(request,'customers/user_detail.html',{'context':context})
    else:
        return HttpResponse("<h1>nothing found</h1>")
def upload(request,name,medi,qty,price):
    bill=Bill()
    bill.name=name
    bill.medi=medi
    bill.qty=qty
    bill.total=price
    a=Stocks_Details.objects.get(medicine=medi)
    qts=a.quantity
    a.quantity=qts-qty
    bill.save()
    a.save()
    forma=Stocks_Details.objects.all()
    forms=form.CreateUser()
    return render(request,'customers/chome.html',{'cdata':forms, 'forma':forma})

