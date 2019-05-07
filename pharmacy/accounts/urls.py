from django.urls import path
from . import views
app_name='accounts-app'

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name="login"),
    path('logout/',views.signout,name="logout")
]