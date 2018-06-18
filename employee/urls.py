from employee import views
from django.conf.urls import url

urlpatterns = [

    url(r'dashboard', views.dashboard, name='dashboard'),

    url(r'emplogin' , views.emplogin, name='emplogin'),
    url(r'empauth', views.empauth, name='empauth'),
    url(r'showrequests', views.showrequests, name='showrequests'),
    url(r'showqueries', views.showqueries, name='showqueries'),

]