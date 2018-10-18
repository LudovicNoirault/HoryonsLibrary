""" Imports """
from django.shortcuts import render

# Create your views here.


def home(request):
    """ function for home """
    return render(request, 'home/home.html')
