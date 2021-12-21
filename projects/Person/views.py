from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.Person.models import MyUser
from projects.Person.serializers import UserSerializer


class UserRegister(CreateAPIView):
    
    model = MyUser
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer


def user_logout(request):
    logout(request)
    return redirect('/')

class MyLoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
