from django.shortcuts import render, redirect
from requests import request

# Create your views here.
def main(request):
    return redirect('drivers')

def drivers(request):
    return render(request, 'main.html')
