""" Imports """
from django.shortcuts import render

# Create your views here.

""" Method used when the used want to play an adv and select it"""


def select(request):
    return render(request, 'PlayAdv/select.html')
