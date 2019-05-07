from django.shortcuts import render
from django.http import HttpResponse
from .models import Stocks_Details
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy
from customers.models import Bill
#import user creation and from here
from django.contrib.auth.decorators import login_required
# Create your views here.
class UpdateStocks(UpdateView):
    model=Stocks_Details
    fields=['company_name','medicine','price','quantity']
    template_name='stocks_details_form.html'
    success_url=reverse_lazy('stocks-app:home')
    
    
class DeleteStocks(DeleteView):
    model=Stocks_Details
    template_name='stocks_details_confirm_delete.html'
    success_url=reverse_lazy('stocks-app:home')
class AddStocks(CreateView):
    model = Stocks_Details
    fields=['company_name','medicine','price','quantity']
    template_name='stocks_add.html'
    success_url=reverse_lazy('stocks-app:home')

def ShowUser(request):
    data=Bill.objects.all()
    return render(request,'user_data.html',{'data':data})

@login_required(login_url='/accounts/login/')
def show(request):
    sd=Stocks_Details.objects.all()
    return render(request,'details.html',{'sd_d':sd})
