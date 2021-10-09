from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50,null=True, blank=True)
    organization = models.CharField(max_length=50,null=True, blank=True, verbose_name="Organization:")
    usertype = models.CharField(max_length=50,null=True,verbose_name="User Type:", default=None, blank=True)
    topic = models.ForeignKey("research.Topic", on_delete=models.CASCADE, default=None, related_name= "teachers",  null=True, blank=True)

class Subject(models.Model):
    title = models.CharField(max_length=50,null=True,verbose_name="Title:")
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
