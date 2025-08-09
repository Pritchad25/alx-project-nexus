from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import RegisterSerializer


User = get_user_model()

class RegisterView(generics.CreateAPIView):
	'''A Registration View.'''
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = []  # Allowing public access
