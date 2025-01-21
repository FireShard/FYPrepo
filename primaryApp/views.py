from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from .models import UserLaptop, LaptopDetails
from .serializers import UserLaptopSerializer, LaptopDetailsSerializer

class UserLaptopViewSet(viewsets.ModelViewSet):
    queryset = UserLaptop.objects.all().order_by('userid')
    serializer_class = UserLaptopSerializer

class LaptopDetailsViewset(viewsets.ModelViewSet):
    queryset = LaptopDetails.objects.all().order_by('laptopid')
    serializer_class = LaptopDetailsSerializer






