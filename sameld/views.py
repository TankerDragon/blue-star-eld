from django.shortcuts import render, redirect
from requests import request
from .models import Driver

# Create your views here.
def main(request):
    return redirect('drivers')

def drivers(request):
    query = Driver.objects.all()
    context = {
        'drivers': query
    }
    return render(request, 'drivers.html', context)

def newDriver(request):
    return render(request, 'new-driver.html')