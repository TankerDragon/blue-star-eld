from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('drivers/', views.drivers, name = 'drivers'),
    path('new-driver/', views.newDriver, name = 'new-driver'),
    path('edit-driver/<int:id>', views.edit_driver, name='edit-driver'),
    path('vehicles/', views.vehicles, name = 'vehicles'),
    path('new-vehicle/', views.newVehicle, name = 'new-vehicle'),
    path('edit-vehicle/<int:id>', views.edit_vehicle, name='edit-vehicle'),
    path('logs/', views.logs, name = 'logs'),
    path('logs/<int:id>', views.log, name = 'log'),
]
