from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from accounts.serializers import RegistrationSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token

class RegisterUser(APIView):
    """
    API For Register User
    """
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                user.set_password(request.data.get("password"))
                token = Token.objects.create(user=user)
                user.save()
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    """
    API For Login User
    """
    def post(self, request, format='json'):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"token": Token.objects.get_or_create(user=user)[0].key}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    """
    API For Logging out user
    """
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({"Logout":"Logged out successfully"}, status=status.HTTP_200_OK)

