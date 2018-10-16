""" Here are the routes for the userPanel app"""
from django.shortcuts import render

# Create your views here.

""" handle the connection fo the user """


def login(request):
    return render(request, 'userPaner/login.html')


"""Handle the registration of the user"""


def register(request):
    return render(request, 'userPaner/register.html')
