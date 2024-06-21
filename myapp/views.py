from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Hello World!")

def hello(request):
    return HttpResponse("Woah that's sick")
