from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('home', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),  
    path('voteInput',views.voteInput, name="voteInput"), 
    path('finalVote',views.finalVote,name="finalVote"),
]


