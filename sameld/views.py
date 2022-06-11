from django.shortcuts import render, redirect
from requests import request
from .models import Driver, Vehicle
from .forms import UserForm, DriverForm, VehicleForm 
from django.contrib.auth.models import User

# Create your views here.
def main(request):
    return redirect('drivers')

def drivers(request):
    query = Driver.objects.all()
    context = {
        'drivers': query,
        'category': 'drivers',
    }
    return render(request, 'drivers.html', context)

def newDriver(request):
    user_form = UserForm()
    driver_form = DriverForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        driver_form = DriverForm(request.POST)
        # print(type(driver_form['user']))
        if user_form.is_valid() and driver_form.is_valid():
            user = user_form.save()
            driver = driver_form.save()
            driver.user = user
            driver.save()

            return redirect('drivers')

    context = {
        'user_form': user_form,
        'driver_form': driver_form,
        'category': 'drivers',
    }
    return render(request, 'new-driver.html', context)

def edit_driver(request, id):
    user = User.objects.get(id=id)
    user_form = UserForm(instance=user)

    driver = Driver.objects.get(user=user)
    driver_form = DriverForm(instance=driver)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        driver_form = DriverForm(request.POST, instance=driver)

        if user_form.is_valid() and driver_form.is_valid():
            user_form.save()
            driver_form.save()
            return redirect('drivers')

    context = {
        'user_form': user_form,
        'driver_form': driver_form,
        'category': 'drivers',
    }
    return render(request, 'new-driver.html', context)

def vehicles(request):
    query = Vehicle.objects.all()
    context = {
        'vehicles': query,
        'category': 'vehicles'
    }
    return render(request, 'vehicles.html', context)

def newVehicle(request):
    vehicle_form = VehicleForm()

    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST)

        if vehicle_form.is_valid():
            vehicle_form.save()
            return redirect('vehicles')

    context = {
        'vehicle_form': vehicle_form,
        'category': 'vehicles',
    }
    return render(request, 'new-vehicle.html', context)

def edit_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle_form = VehicleForm(instance=vehicle)

    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST, instance=vehicle)

        if vehicle_form.is_valid():
            vehicle_form.save()
            return redirect('vehicles')

    context = {
        'vehicle_form': vehicle_form,
        'category': 'vehicles',
    }
    return render(request, 'new-vehicle.html', context)






#         new_driver = Driver()
#         new_driver.user = user
#         new_driver.cdl_number = request.POST.get('cdl_number')
#         new_driver.cdl_state = request.POST.get('cdl_state')
#         if request.POST.get('vehicle'):
#             new_driver.vehicle = request.POST.get('vehicle')
#         else:
#             new_driver.vehicle = NULL
#         new_driver.co_driver = request.POST.get('co_driver')
#         new_driver.company_user_id = request.POST.get('company_user_id')
#         new_driver.phone = request.POST.get('phone')
#         new_driver.notes = request.POST.get('notes')
#         new_driver.save()
#         # Drivers.objects.create()