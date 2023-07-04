from rest_framework import serializers
from .models import User, Profile, App
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

#         def create(self, validated_data):
#             user = User.objects.create(
#                 username=validated_data["password"], password=make_password(validated_data["password"]))
#             user.save()
#             # Token.objects.create(user=user)
#             return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class AdminAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'points', 'complete')


class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'


class CreateAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
