from employee import views
from django.conf.urls import url

urlpatterns = [

    url(r'dashboard', views.dashboard, name='dashboard'),

    url(r'login' , views.emplogin, name='emplogin'),
    url(r'empauth', views.empauth, name='empauth'),
    url(r'showrequests', views.showrequests, name='showrequests'),
    url(r'showqueries', views.showqueries, name='showqueries'),
url(r'logout', views.logout, name='logout'),

]