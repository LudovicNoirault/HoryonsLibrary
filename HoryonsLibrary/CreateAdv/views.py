"""Imports"""
from django.shortcuts import render

# Create your views here.


def create(request):
    """ Method used when we create an adventure"""
    return render(request, 'CreateAdv/create.html')
