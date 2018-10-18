""" Imports """
from django.shortcuts import render

# Create your views here.


def select(request):
    """ Method used when the used want to play an adv and select it"""
    return render(request, 'PlayAdv/select.html')
