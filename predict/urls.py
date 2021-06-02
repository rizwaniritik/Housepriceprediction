from django.contrib import admin
from django.urls import path
from predict import views

urlpatterns = [
   path("",views.home,name="home"),
   path("/",views.home,name="home"),
  

]