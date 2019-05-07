from django.urls import path
from . import views
app_name='customers'

urlpatterns=[
    path('',views.home),
    path('save',views.save),
    path('<str:name>/<str:medi>/<int:qty>/<int:price>',views.upload),
]