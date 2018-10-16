"""Imports"""
from django.shortcuts import render

# Create your views here.

""" Method used when we create an adventure"""


def create(request):
    return render(request, 'CreateAdv/create.html')
