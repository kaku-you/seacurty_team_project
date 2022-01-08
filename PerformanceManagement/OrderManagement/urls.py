from django.conf.urls import url
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('ka', views.kakikomi, name='kakikomi'),
    url('tm', views.tmperatureform, name='tmperatureform'),
    ]