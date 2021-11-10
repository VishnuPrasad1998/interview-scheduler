from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'groups']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length=128)
    class Meta:
        model = User
        fields = ['username', 'password']

