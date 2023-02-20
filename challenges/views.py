from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(httpRequest):
    return HttpResponse("this works!")

def february(httpRequest):
    return HttpResponse("february")

def monthlyChallenge(httpRequest,month):
    challenge_text = "not fount!"
    if month == "january":
        challenge_text = "january challenge"
    elif month == "february":
        challenge_text = "february challenge"
    elif month == "march":
        challenge_text = "march challenge"
    else:
        return HttpResponseNotFound("Not fount")
    return HttpResponse(challenge_text)
        
