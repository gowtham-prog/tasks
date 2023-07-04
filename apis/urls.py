from django.urls import path, include
from .views import index, login_view, register, app, getapp, listapp, saveapp, profile, LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('register', register.as_view(), name='register'),
    path('login', login_view.as_view(), name="login"),
    path('adminapp', app.as_view(), name="app"),  # admin tasks creation
    path('allapps', listapp.as_view(), name="applist"),  # admin task
    path('getapp/<int:pk>', getapp.as_view(),
         name="getapp"),  # retrive app based on id
    path('saveapp', saveapp.as_view(), name="saveapp"),  # save app
    path('profile/<int:pk>', profile.as_view(), name="profile"),
    path('logout',  LogoutView, name='logout'),
]
