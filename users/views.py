from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    '''Defines a Views.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
