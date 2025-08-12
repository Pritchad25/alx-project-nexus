"""nexus_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path, include
from users.views import RegisterView
from django.contrib import admin
from products.views import ProductViewSet
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
        path('api/', include(router.urls)),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('admin/', admin.site.urls),
        path('users/', include('users.urls')),
]
urlpatterns += [
        path('api/register/', RegisterView.as_view(), name='register'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

