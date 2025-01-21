from django.shortcuts import render
from django.http import JsonResponse
from .models import RamDetails, LaptopDetails, UserLaptop
from rest_framework import permissions, viewsets
from .serializers import RamDetailsSerializer, LaptopDetailsSerializer, UserLaptopSerializer

# Create your views here.
