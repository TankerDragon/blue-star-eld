from re import L
from django.contrib import admin
from .models import Driver, Vehicle, Log
# Register your models here.
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Log)