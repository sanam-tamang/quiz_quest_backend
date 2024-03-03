
from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewset, basename="user")


urlpatterns = [
    path('', include(router.urls)),
]