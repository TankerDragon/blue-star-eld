from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Driver



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        # ['user_id', 'cdl_number', 'vehicle_id', 'notes']
        fields = ['cdl_number', 'cdl_state', 'vehicle', 'company_user_id', 'phone',
                  'co_driver', 'notes']

# class VehicleForm(ModelForm):
#     class Meta:
#         model = Vehicle
#         fields = '__all__'