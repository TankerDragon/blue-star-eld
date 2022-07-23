from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
####
from sameld.models import Driver
from .serializers import DriverSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def drivers(request):
    if request.method == 'GET':
        queryset = Driver.objects.all()
        serializer = DriverSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
    return HttpResponse('Fuck?')