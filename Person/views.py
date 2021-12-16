from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView

from Person.models import MyUser
from Person.serializers import UserSerializer


class UserRegister(CreateAPIView):
    
    model = MyUser
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer
