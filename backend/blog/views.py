from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Post
from .serializer import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.filter(active=True).order_by('title')
	serializer_class = PostSerializer
    #permission_classes = [permissions.IsAuthenticated]