from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import BasicAuthentication

# Create your views here.


@permission_classes((IsAuthenticated,))
def admin(request):
    return render(request, "users/admin.html")


# @login_required(login_url="main-login")
def user(request):
    return render(request, "users/user.html")


def login(request):
    return render(request, "users/login.html")
