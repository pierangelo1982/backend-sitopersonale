from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Page
from .serializer import PageSerializer


class PageViewSet(viewsets.ModelViewSet):
	queryset = Page.objects.filter(active=True).order_by('title')
	serializer_class = PageSerializer
    #permission_classes = [permissions.IsAuthenticated]
