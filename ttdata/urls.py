from lib2to3.pgen2 import driver
from django.urls import path
from .views import drivers

urlpatterns = [
    path('', drivers)
]
