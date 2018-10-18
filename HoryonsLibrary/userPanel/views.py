""" Here are the routes for the userPanel app"""
from django.shortcuts import render

# Create your views here.


def login(request):
    """ handle the connection fo the user """
    return render(request, 'userPaner/login.html')


def register(request):
    """Handle the registration of the user"""

    return render(request, 'userPaner/register.html')
