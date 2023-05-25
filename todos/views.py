from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, TodoSerializer
from .models import Todo


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().filter()
    serializer_class = TodoSerializer
    permission_classes = [AllowAny]
