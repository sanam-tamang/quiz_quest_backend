
from rest_framework import viewsets
from account.models import CustomUser
from .serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer