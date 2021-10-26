from django.shortcuts import render
from .models import Room
# Create your views here.

def home(request):
    rooms = Room.objects.all() #get data from database
    context = {'rooms': rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request=request,template_name='base/room.html',context=context)