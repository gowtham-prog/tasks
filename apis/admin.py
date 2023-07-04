from django.contrib import admin
from .models import User, Profile, App
# Register your models here.
admin.site.register(App)
admin.site.register(Profile)