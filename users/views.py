from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    '''A User View'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class RegisterView(generics.CreateAPIView):
	'''A Registration View.'''
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = []  # Allowing public access
