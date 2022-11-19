from django.contrib import admin
from django.urls import path
from MyWebsite import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('index2', views.index2, name = "home2"),
    path('about', views.about, kwargs = {"name": "Danila"}),
]
