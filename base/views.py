from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request=request,template_name='home.html')

def room(request):
    return render(request,'room.html')