from django.shortcuts import render
from django.http import HttpResponse 
from datetime import date 

def check(request):
    current_day = date.today().day
    current_month = date.today().month

    return render(request,"check.html")
