from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request=request,template_name='home.html')

def room(request):
    return render(request,'room.html')