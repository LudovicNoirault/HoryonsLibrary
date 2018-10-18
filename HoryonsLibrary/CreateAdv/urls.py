"""Import"""
from django.urls import path
from . import views

urlpatterns = [
    # Routes creation of the adventure
    path('', views.create, name="create"),
]
