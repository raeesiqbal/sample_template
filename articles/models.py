from django.urls import reverse
from django.db import models
from users.models import User
from ckeditor.fields import RichTextField


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="user",  null=True)
    title = models.CharField(max_length=50, null=True, verbose_name="Title:")
    slug = models.SlugField(max_length=100, default=None, null=True,  blank=True)
    mini_detail = models.CharField(max_length=50, null=True, blank=True, verbose_name="Content:")
    subject = models.CharField(max_length=50, null=True, blank=True, verbose_name="Subject:")
    image = models.ImageField(null=True, blank=True, verbose_name="Image")
    content = RichTextField(blank=True, null=True, verbose_name="Content")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', args=[self.slug])


class Subject(models.Model):
    title = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
