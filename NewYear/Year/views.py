from django.shortcuts import render
from django.http import HttpResponse 
from datetime import date 

def check(request):
    current_day = int(date.today().day)
    current_month = int(date.today().month)
    if current_month == 1 and current_day == 1:
        return render(request,"check.html",{'checking':'YES',})
    else:
        return render(request,"check.html",{'checking':'NO',})
        

    
