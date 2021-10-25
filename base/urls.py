from django.urls import path
from . import views

urlpatterns:list = [
    path('', views.home, name="home"),
    path('rooms/<str:pk>', views.room, name="room"),
]