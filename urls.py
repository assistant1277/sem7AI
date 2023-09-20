from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
   path("index",views.index, name='index'),
   path("about",views.about, name='about'),
   path("signup",views.handlesignup, name='signup'),
   # path("login.html",views.handlelogin, name='login'),
   path("login",views.handlelogin, name='login'),
]
