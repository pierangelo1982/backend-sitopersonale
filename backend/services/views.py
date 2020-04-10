from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Service
from .serializer import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
	queryset = Service.objects.filter(active=True).order_by('title')
	serializer_class = ServiceSerializer
    #permission_classes = [permissions.IsAuthenticated]

