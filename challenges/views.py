from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenge_map ={
    "january":"january",
    "test":"new"
}


def index(httpRequest):
    return HttpResponse("this works!")

def february(httpRequest):
    return HttpResponse("february")

def monthlyChallenge(httpRequest,month):
    try:
        challenge_text = monthly_challenge_map[month] 
    except:
        return HttpResponseNotFound("Not fount")
    return HttpResponse(challenge_text)
        
