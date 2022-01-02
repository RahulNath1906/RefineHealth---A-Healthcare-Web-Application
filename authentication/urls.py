from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('index2',views.index2, name = "index2"),
    path('signin',views.signin, name="signin"),
    path('signup',views.signup, name="signup"),
    path('signout',views.signout, name="signout"),
    path('ambulance',views.ambulance, name="ambulance"),
    path('covid',views.covid, name="covid"),

]
