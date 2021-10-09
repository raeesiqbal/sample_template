from users.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Topic(models.Model):
    title = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="researchuser",  null=True)
    title = models.CharField(max_length=50, null=True, verbose_name="Subject:")
    main_image = models.ImageField(null=True, blank=True, verbose_name="Image")
    file = models.FileField(null=True, blank=True, verbose_name="File")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None, related_name="projectopic",  null=True)
    content = RichTextField(blank=True, null=True, verbose_name="Content")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="ideauser",  null=True)
    title = models.CharField(max_length=50, null=True, verbose_name="Subject:")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None, related_name="ideatopic",  null=True)
    content = RichTextField(blank=True, null=True, verbose_name="Content")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }
