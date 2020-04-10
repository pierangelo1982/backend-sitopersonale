from django.urls import path, include
from rest_framework import routers
from .views import PageViewSet

router = routers.DefaultRouter()
router.register('pages', PageViewSet)

urlpatterns = [
    path('', include(router.urls))
]