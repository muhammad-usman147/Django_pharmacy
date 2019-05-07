from django.urls import path,include
from . import views
app_name='mainapp'

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('stocks/',include('stocks.urls')),
    path('accounts/',include('accounts.urls')),
    path('customers/',include('customers.urls')),
]
