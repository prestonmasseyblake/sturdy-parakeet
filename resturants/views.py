from django.shortcuts import render
from .models import Resturant, Deal
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from .serializers import ResturantSerializer
# Create your views here.
class ResturantView(viewsets.ModelViewSet):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializer
