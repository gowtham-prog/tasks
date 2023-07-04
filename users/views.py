from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import BasicAuthentication

# Create your views here.


@login_required(login_url='main-login')
def admin(request):
    if not request.user.is_superuser:
        return render(request, "users/login.html")
    return render(request, "users/admin.html")


@login_required(login_url="main-login")
def user(request):
    return render(request, "users/user.html")


def login(request):
    return render(request, "users/login.html")
