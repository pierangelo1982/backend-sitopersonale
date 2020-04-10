from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Slider
from .serializer import SliderSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Slider.objects.filter(active=True).order_by('-pub_date')
	serializer_class = SliderSerializer
    #permission_classes = [permissions.IsAuthenticated]
