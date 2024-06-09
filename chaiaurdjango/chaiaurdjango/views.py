from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'websides/index.html')

def about(request):
    return HttpResponse("hello,world. you are at chai aur Django about")

def contact(request):
    return HttpResponse("hello,world. you are at chai aur Django contact page")
