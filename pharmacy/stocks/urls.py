from django.urls import path
from . import views
app_name='stocks-app'
urlpatterns=[
    path('',views.show,name='home'),
    path('update/<pk>/',views.UpdateStocks.as_view(),name='update_stock'),
    path('delete/<pk>/',views.DeleteStocks.as_view(),name='delete_stock'),
    path('add/',views.AddStocks.as_view(),name='add-stock'),
    path('showuser',views.ShowUser,name='show-user')
]