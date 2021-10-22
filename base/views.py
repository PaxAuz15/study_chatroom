from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(responnse):
    return HttpResponse("Home View")

def room(response):
    return HttpResponse("ROOM")