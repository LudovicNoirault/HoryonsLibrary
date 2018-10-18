""" Imports """
from django.urls import path
from . import views

urlpatterns = [
    # Routes selection of the adventure
    path('', views.select, name="select"),
]
