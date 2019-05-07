from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def homepage(request):
    return render(request,'accounts/select.html')
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stocks-app:home')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})
def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            users=form.get_user()
            login(request,users)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('stocks-app:home')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
def signout(request):
    if request.method=='POST':
        logout(request)
        return redirect('mainapp:homepage')