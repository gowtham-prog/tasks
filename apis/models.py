from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    tasks = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} ==> {self.user.username}'


class App(models.Model):
    file = models.FileField(upload_to="files/", null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False, blank=False)
    points = models.IntegerField(null=False, blank=False, default=0)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id} . {self.name} --  edited by - {self.user}"
