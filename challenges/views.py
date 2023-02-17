from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(httpRequest):
    return HttpResponse("this works!")

def february(httpRequest):
    return HttpResponse("february")
        
