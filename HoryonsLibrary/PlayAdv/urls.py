"""Imports"""
from django.urls import path
from . import views

""" Routes for the PlayAdv app"""
urlpatterns = [
    path('', views.select, name="select"),
]
