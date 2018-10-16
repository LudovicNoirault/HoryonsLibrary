""" Here are the routes for the userPanel app"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
]
