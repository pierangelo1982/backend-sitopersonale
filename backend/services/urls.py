from django.urls import path, include
from rest_framework import routers
from .views import ServiceViewSet

router = routers.DefaultRouter()
router.register('services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls))
]
