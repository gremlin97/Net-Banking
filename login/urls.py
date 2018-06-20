from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views

urlpatterns = [

url(r'^$' , views.index , name='indexpage'),
url(r'^login' , views.login , name='loginpage'),
url(r'^about', views.about, name='about'),
url(r'^contact', views.contact, name='contact'),
url(r'^gallery',views.gallery, name='gallery'),
url(r'^services', views.services, name='services'),
url(r'^index', views.index, name='index'),

url(r'^authenticate', views.authenticate, name="authenticate"),
url(r'^register', views.register, name='register'),
url(r'^valregistration', views.valregistration, name='valregistration'),
url(r'^dashboard', views.Dashboard, name='Dashboard'),
url(r'^transact', views.transact, name='transact'),
url(r'^requestservices', views.requestservices, name='requestservices'),
url(r'^resetpass', views.resetpass, name='resetpass'),
url(r'^showtransactions', views.showtransactions, name='showtransactions'),
url(r'^checkbal', views.checkbal, name='checkbal'),
url(r'^submitquery', views.submitquery, name='submitquery'),
url(r'^checkbal', views.checkbal, name='checkbal'),
url(r'^logout', views.logout, name='logout'),




]