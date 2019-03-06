from django.urls import path
from . import views
appname='stocks'
urlpatterns=[
    path('',views.show),
]