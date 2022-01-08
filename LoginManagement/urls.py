from django.conf.urls import url
from . import views

#urlpatterns = [
#    url(r'^$', views.AccountRegistration.as_view(), name='registration'),
#]

urlpatterns = [
    url(r'^$',views.Login,name='Login'),
    url("logout",views.Logout,name="Logout"),
    url('register',views.AccountRegistration.as_view(), name='register'),
    url("home",views.home,name="home"),
]