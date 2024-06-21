from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path("", views.home, name="home"),
    path("hello", views.hello, name="waddup")
]