from django.urls import path, include
from . import views

urlpatterns = [
    path("user", views.user, name="user"),
    path("admin", views.admin, name="admin")
]
