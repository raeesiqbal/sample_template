from django.db import models
from users.models import User
from ckeditor.fields import RichTextField


class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="threaduser",  null=True)
    title = models.CharField(max_length=50, null=True, verbose_name="Title:")
    subject = models.CharField(max_length=50, null=True, verbose_name="Subject:")
    mini_detail = models.CharField(max_length=50, null=True, blank=True, verbose_name="MiniDetail:")
    image = models.ImageField(null=True, blank=True, verbose_name="Image")
    content = RichTextField(blank=True, null=True, verbose_name="Content")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
