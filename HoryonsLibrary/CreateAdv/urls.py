"""Import"""
from django.urls import path
from . import views

""" Routes for the CreateAdv app"""
urlpatterns = [
    path('', views.create, name="create"),
]
