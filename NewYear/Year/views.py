from django.shortcuts import render
from django.http import HttpResponse 


def check(request):
    return HttpResponse("Hello World !!!")
