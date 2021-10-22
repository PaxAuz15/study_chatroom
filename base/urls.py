from django.urls import path
from . import views

urlpatterns:list = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
]