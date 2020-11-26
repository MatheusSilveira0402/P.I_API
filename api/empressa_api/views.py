from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, EmpressaSerializer
from .models import Empressa
from rest_framework_api_key.permissions import HasAPIKey
#

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated | HasAPIKey]

class EmpressaViewSet(viewsets.ModelViewSet):
    queryset = Empressa.objects.all()
    serializer_class = EmpressaSerializer
    permission_classes = [permissions.IsAuthenticated | HasAPIKey]