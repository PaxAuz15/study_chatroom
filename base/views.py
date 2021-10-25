from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name': 'Lets learn python!'},
    {'id':2, 'name': 'Design with me!'},
    {'id':3, 'name': 'Frontends Developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request,'home.html',context)

def room(request):
    return render(request=request,template_name='room.html')