from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import generics, viewsets
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from ratelimit.decorators import ratelimit

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
	permission_classes = []  # Allowing public acces

@csrf_exempt
@ratelimit(key='ip', rate='5/m', block=True)
def login_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    username = data.get('username')
    password = data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        return JsonResponse({'message': 'Login successful'})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
